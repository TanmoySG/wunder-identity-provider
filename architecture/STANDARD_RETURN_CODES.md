# Standardized Return Code Guide

This Documentation contains the details of various standard return codes used througout the project.

## AuthLib Return Codes

Refer to [providers/authlib/standards/return_codes.py](../providers/authlib/standards/return_codes.py) file.

```
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
        "response": "failure"
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
```

## LoginProvider Return Codes

Refer to [providers/loginProvider/standards/return_codes.py](../providers/loginProvider/standards/return_codes.py) file.

```
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
```

## RegistrationProvider Return Codes

Refer to [providers/registrationProvider/standards/return_codes.py](../providers/registrationProvider/standards/return_codes.py) file.

```
    RPR01 = {
        "return_code": "RPR01",
        "scope": "registration.register.verified",
        "details": "Profile Created. Welcome Mail Sent.",
        "response": "success"
    }

    RPR02 = {
        "return_code": "RPR02",
        "scope": "registration.register.verified",
        "details": "Profile already exists.",
        "response": "failure"
    }
```

## Mailer Return Codes

Refer to [providers/mailer/standards/return_codes.py](../providers/mailer/standards/return_codes.py) file.

```
    MLS01 = {
        "return_code": "MLS01",
        "scope": "mailer.send.mail",
        "details": "Mail Sent!",
        "response": "success"
    }

    # Failure Case - Yet to be Implemented
    MLS02 = {
        "return_code": "MLS02",
        "scope": "mailer.send.mail",
        "details": "Could not send mail.",
        "response": "failure"
    }
```