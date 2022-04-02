import json
import sys

from flask import Flask, jsonify, redirect, request, send_from_directory
from flask_cors import CORS
# from logsmith import log

from providers.request_processor import REQUEST_PROCESSOR

# # Setup Logsmith
# log = log()
# log.configure(ENV="DEV", logfile="logs", console_only=True)

app = Flask(__name__)
CORS(app)


# New Registration Endpoint
@app.route("/register/generate", methods=['POST'])
def new_registration_request():
    request_data = request.get_json(force=True)
    response = REQUEST_PROCESSOR().new_registration_request_processor(
        request_data=request_data
    )
    return response


@app.route("/register/verify", methods=["POST"])
def account_verification_request():
    request_data = request.get_json(force=True)
    response = REQUEST_PROCESSOR().account_verification_request_processor(
        request_data=request_data
    )
    return response


if __name__ == '__main__':
    app.run(debug=True)