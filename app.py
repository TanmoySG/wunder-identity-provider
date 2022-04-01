import json
import sys

from flask import Flask, jsonify, redirect, request, send_from_directory
from flask_cors import CORS
from logsmith import log

from providers.authLib.authLib import AUTHLIB
from providers.authLib.standards.return_codes import RETURN_CODES as AL_RC

from providers.loginProvider.login import LOGIN
from providers.loginProvider.standards.return_codes import RETURN_CODES as LG_RC

from providers.mailer.content import CONTENT_FACTORY
from providers.mailer.mailer import MAILER
from providers.mailer.standards.return_codes import RETURN_CODES as ML_RC

from providers.registrationProvider.registration import REGISTER
from providers.registrationProvider.standards.return_codes import RETURN_CODES as RG_RC

from providers.response_factory import RESPONSE_FACTORY

# Setup Logsmith
log = log()
log.configure(ENV="DEV", logfile="logs", console_only=True)

app = Flask(__name__)
CORS(app)



@app.route("/register/generate", methods = ['POST'])
def new_registration_request():
    request_data = request.get_json(force = True)

    response, _ = AUTHLIB().register(
        mailID=request_data["email"],
        username=request_data["name"],
        password=request_data["password"]
    )

    if response == AL_RC.ALR02:
        REGISTRATION_MAILER = MAILER(mailer_mode=CONTENT_FACTORY.VERIFIED_MAIL)
        REGISTRATION_MAILER.prepare_mail(payload=request_data["email"])
        response = REGISTRATION_MAILER.send_mail(request_data["email"])

        if response == ML_RC.MLS01:
            log.INFO(response["details"])
            return {}
        else:
            log.WARN(response["details"])
    else:
        log.WARN(response["details"])

    
