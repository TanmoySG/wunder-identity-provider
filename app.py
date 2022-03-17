import hashlib, json, string, random, secrets, shortuuid
from flask import Flask, request, jsonify, redirect, send_from_directory
from os import path, write
from flask_cors import CORS
from datetime import datetime
import smtplib, ssl, time, hashlib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


app = Flask(__name__)

CORS(app)

server_credentials = json.load(open('server-config.json'))

port = server_credentials['port']
serverAddress = server_credentials['mail-server']
sender = server_credentials['sender']
password = server_credentials['password']

def write_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
        
def hash_otp(mail, otp, timestamp):
    complete_string = mail+"."+otp+"."+timestamp
    return hashlib.md5(complete_string.encode()).hexdigest()
        
def generate_OTP():
    return ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits , k = 6))

def send_mail(recipient, mail_template, content):
    message = MIMEMultipart("alternative")
    message["Subject"] = content["subject"]
    message["From"] = sender
    message["To"] = recipient
    template = open(mail_template).read().replace(content["replacement_token"], content["replacement_string"])
    html = MIMEText(template, "html")
    message.attach(html)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(serverAddress, port, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, recipient, message.as_string())


def generate_mail(recipient, mode, payload="none"):
    if mode=="generate-otp-mail":
        content = {
            "subject" : "Verify you wunderDB account",
            "replacement_token": "%otp%",
            "replacement_string": payload["otp"]
        }

        send_mail(recipient, "emailTemplates/otp_generation_template.html", content)

    elif mode=="verified-otp-mail":
        content = {
            "subject" : "Account Verified.",
            "replacement_token": "%user%",
            "replacement_string": recipient
        }
        send_mail(recipient, "emailTemplates/otp_verified_template.html", content)


def create_new_request(mail, otp):
    with open("authlib.json") as authlib:
        authdict = json.load(authlib)
        if mail not in authdict.keys():
            ts = time.time()
            timestamp = datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            authdict[mail] = {
                "mail" : mail,
                "timestampLatestOTP": timestamp ,
                "latestOTP": hash_otp(mail, otp, timestamp),
                "status" : "unverified"
            }
            write_json(authdict, "authlib.json")
            generate_mail(mail, "generate-otp-mail", {"otp": otp})
            return "Created"
        else:
            generate_mail(mail, "generate-otp-mail", {"otp": authdict[mail]["latestOTP"]})
            print("Request Exists")

@app.route("/register/authenticate", methods = ['POST'])
def initialize_new_authentication():
    incoming_data = request.get_json(force = True)
    with open("users.json", 'r') as users:
        user = json.load(users)
        users_list = user['users']
        if incoming_data['username'] not in users_list.keys():    
            otp = generate_OTP()
            create_new_request(incoming_data['username'], otp)
            return jsonify({ 
                "status_code" : '1',
                "response" : "OTP Sent." 
            })
        else:
            return jsonify({ 
                "status_code" : '1',
                "response" : "User Exists." 
            })

@app.route("/register/verify", methods = ['POST'])
def authenticate_OTP():
    incoming_data = request.get_json(force = True)
    mail = incoming_data['username']
    otp = incoming_data['otp']
    with open("authlib.json") as authlib:
        temp = json.load(authlib)
        if mail in temp.keys():
            if temp[mail]["latestOTP"] == hash_otp(mail, otp, temp[mail]["timestampLatestOTP"]):
                temp.pop(mail)
                write_json(temp, "authlib.json")
                generate_mail(mail, "verified-otp-mail")
                print("Verified")
                return register(incoming_data)
            else:
                print("Wrong OTP")
                return jsonify({ 
                    "status_code" : '0',
                    "response" : "Wrong OTP." 
                })
        else:
            return jsonify({ 
                "status_code" : '0',
                "response" : "User already exists." 
            })


# CREATE CLUSTER / REGISTER
# @app.route('/register', methods = ['POST'])
def register(user_data):
    with open("users.json", 'r') as users:
        user = json.load(users)
        users_list = user['users']
        if user_data['username'] not in users_list.keys():
            salt = user_data['username'].encode('utf-8')
            hashed_password = hashlib.sha512(user_data['password'].encode('utf-8') + salt).hexdigest()

            tokens = []
            cluster_id =shortuuid.uuid()
            for _ in range(3):
                tokens.append(secrets.token_hex(16))
            
            user_init = {
                "_cluster_id" : cluster_id,
                "name" : user_data['name'],
                "username" : user_data['username'],
                "password" : hashed_password,
                "access_tokens": tokens
            }

            users_list[user_data['username']] = user_init
            write_json(user, 'users.json')

            return jsonify({ 
                "status_code" : '1',
                "response" : "Cluster Created",
                "cluster_id" : cluster_id , 
                "access_tokens" : tokens
                })
        else:
            return jsonify({ 
                "status_code" : '0',
                "response" : "User already exists." 
                
            })

# LOGIN
@app.route('/login', methods = ['POST'])
def login():
    user_data = request.get_json(force = True)
    file = "users.json"
    with open(file) as user_list:
        users = json.load(user_list)
        user = users['users']
        if user_data["username"] in user.keys():
            salt = user_data['username'].encode('utf-8')
            hashed_password = hashlib.sha512(user_data['password'].encode('utf-8') + salt).hexdigest()
            if user[user_data["username"]]['username'] == user_data['username'] and user[user_data["username"]]['password'] == hashed_password :
                return jsonify({
                    "status_code" : '1',
                    "response" : "Logged-in",
                    "name" : user[user_data["username"]]['name'],
                    "cluster_id" : user[user_data["username"]]['_cluster_id'],
                    "access_token" : random.choice(user[user_data["username"]]['access_tokens'])
                })
            else:
                return jsonify({
                    "status_code" : '0',
                    "response" : "Password is wrong."
            })
        else:
            return jsonify({
                "status_code" : '0',
                "response" : "User doesn't exist"
            })
      
@app.route("/")
def main():
    return {"response" : "Welcome to AuthLib v2.0"}