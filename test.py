from time import sleep
from providers.authLib.authLib import AUTHLIB
from providers.registrationProvider.registration import REGISTER
from providers.authLib.standards.return_codes import RETURN_CODES

sample_user = {
    "email": "random@mail.com",
    "name": "Joh Doe",
    "password": "123456"
}

response, otp = AUTHLIB().register(
    mailID=sample_user["email"],
    username=sample_user["name"],
    password=sample_user["password"]
)

print("Step-1: Registered")
print(response, otp)

sleep(5)

response, profile = AUTHLIB().verify(
    mailID=sample_user["email"],
    user_supplied_secret=otp
)

print("Step-2: Verification")
print(response, profile)

sleep(2)

if response == RETURN_CODES.ALR14:
    REGISTER().register_verified_profile(verified_profile=profile)
else:
    print("Out")