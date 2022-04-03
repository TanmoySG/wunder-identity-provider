from crypt import methods
from flask import Flask, request
from flask_cors import CORS

from providers.request_processor import REQUEST_PROCESSOR

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["POST"])
def index():
    return "<h1>Welcome to wIP API</h1>"


# New Registration Endpoint
@app.route("/register/generate", methods=['POST'])
def new_registration_request():
    request_data = request.get_json(force=True)
    response = REQUEST_PROCESSOR().new_registration_request_processor(
        request_data=request_data
    )
    return response


# Account Verification Endpoint
@app.route("/register/verify", methods=["POST"])
def account_verification_request():
    request_data = request.get_json(force=True)
    response = REQUEST_PROCESSOR().account_verification_request_processor(
        request_data=request_data
    )
    return response


# Login Endpoint
@app.route("/login", methods=["POST"])
def account_login_request():
    request_data = request.get_json(force=True)
    response = REQUEST_PROCESSOR().account_login_request_processor(
        request_data=request_data
    )
    return response


if __name__ == '__main__':
    app.run(debug=True)
