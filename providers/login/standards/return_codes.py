class RETURN_CODES:

    LPR01 = {
        "return_code": "LPR01",
        "scope": "login.profile.email",
        "details": "Invalid Email",
        "response": "failure"
    }

    LPR02 = {
        "return_code": "LPR02",
        "scope": "login.profile.email",
        "details": "Account does not exist for this Email.",
        "response": "failure"
    }

    LPR03 = {
        "return_code": "LPR03",
        "scope": "login.profile.password",
        "details": "Password Doesn't Match. Login Failed.",
        "response": "failure"
    }

    LPR04 = {
        "return_code": "LPR04",
        "scope": "login.profile.verified",
        "details": "Account Verified. Login Successful.",
        "response": "success"
    }