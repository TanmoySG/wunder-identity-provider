# Return Codes
class RETURN_CODES:
    ALR01 = {
        "scope": "authlib.requests.register",
        "details": "Invalid Email Address",
        "response": "fail"
    }
    ALR02 = {
        "scope": "authlib.requests.register",
        "details": "Request Registered Successfully. OTP Generated.",
        "response": "success"
    }
    ALR03 = {
        "scope": "authlib.requests.register",
        "details": "Invalid Email Address",
        "response": "Failed"
    }
    ALR11 = {
        "scope": "authlib.requests.verify",
        "details": "Mail Doaesn't Exist in AuthLib. Re-Register with details.",
        "response": "Failed"
    }
    ALR12 = {
        "scope": "authlib.requests.verify",
        "details": "Authentication Request Expired. OTP Re-generated.",
        "response": "Failed"
    }
    ALR13 = {
        "scope": "authlib.requests.verify",
        "details": "Incorrect OTP. Authentication Failed.",
        "response": "Failed"
    }
    ALR14 = {
        "scope": "authlib.requests.verify",
        "details": "Correct OTP. Authentication Successful.",
        "response": "Success"
    }
    ALR15 = {
        "scope": "authlib.requests.verify",
        "details": "OTP Expired. Authentication Failed.",
        "response": "Failed"
    }
