# Return Codes
class RETURN_CODES:
    ALR01 = {
        "return_code": "ALR01",
        "scope": "authlib.requests.register",
        "details": "Invalid Email Address",
        "response": "failure"
    }
    ALR02 = {
        "return_code": "ALR02",
        "scope": "authlib.requests.register",
        "details": "Request Registered Successfully. OTP Generated.",
        "response": "success"
    }
    ALR03 = {
        "return_code": "ALR03",
        "scope": "authlib.requests.register",
        "details": "Request Exists. Check your Mail.",
        "response": "success"
    }
    ALR11 = {
        "return_code": "ALR11",
        "scope": "authlib.requests.verify",
        "details": "Mail Doaesn't Exist in AuthLib. Re-Register with details.",
        "response": "failure"
    }
    ALR12 = {
        "return_code": "ALR12",
        "scope": "authlib.requests.verify",
        "details": "Authentication Request Expired. OTP Re-generated.",
        "response": "failure"
    }
    ALR13 = {
        "return_code": "ALR13",
        "scope": "authlib.requests.verify",
        "details": "Incorrect OTP. Authentication Failed.",
        "response": "failure"
    }
    ALR14 = {
        "return_code": "ALR14",
        "scope": "authlib.requests.verify",
        "details": "Correct OTP. Authentication Successful.",
        "response": "success"
    }
    ALR15 = {
        "return_code": "ALR15",
        "scope": "authlib.requests.verify",
        "details": "OTP Expired. Authentication Failed.",
        "response": "failure"
    }
