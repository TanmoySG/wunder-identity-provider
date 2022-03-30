from time import sleep
from providers.authLib.authLib import AUTHLIB
from providers.registrationProvider.registration import REGISTER
from providers.authLib.standards.return_codes import RETURN_CODES as AUTHLIB_RC
from providers.mailer.mailer import MAILER
from providers.mailer.standards.return_codes import RETURN_CODES as MAILER_RC
from providers.mailer.content import CONTENT_FACTORY
from providers.registrationProvider.standards.return_codes import RETURN_CODES as RRC
from providers.loginProvider.login import LOGIN
from providers.loginProvider.standards.return_codes import RETURN_CODES as LRC


from logsmith import log

# Setup Logsmith
log = log()
log.configure(ENV="DEV", logfile="logs", console_only=True)

sample_user = {
    "email": "tanmoysps@gmail.com",
    "name": "Joh Doe",
    "password": "123456"
}
print("--------------------------------------------")
print("End-to-End Registration Flow Start")
print("--------------------------------------------")
# Register New User 
response, otp = AUTHLIB().register(
    mailID=sample_user["email"],
    username=sample_user["name"],
    password=sample_user["password"]
)

log.INFO(response)

sleep(1)

# Mail OTP
if response == AUTHLIB_RC.ALR02:
    MAILER_1 = MAILER(mailer_mode=CONTENT_FACTORY.OTP_MAIL)
    MAILER_1.prepare_mail(payload=otp)
    response = MAILER_1.send_mail(sample_user["email"])

    log.INFO(response)

sleep(1)

# Verify Account with OTP
response, profile = AUTHLIB().verify(
    mailID=sample_user["email"],
    user_supplied_secret=otp
)

log.INFO(response)

sleep(1)

# Register Verified Profile
if response == AUTHLIB_RC.ALR14:
    response = REGISTER().register_verified_profile(verified_profile=profile)
    log.INFO(response)

    sleep(1)

    # Mail User on Successful Verification
    if response == RRC.RPR01:
        MAILER_2 =  MAILER(mailer_mode=CONTENT_FACTORY.VERIFIED_MAIL)
        MAILER_2.prepare_mail(payload=sample_user["email"])
        response = MAILER_2.send_mail(sample_user["email"])

        log.INFO(response)


log.SUCCESS("End-to-End Registration Flow Complete")

sleep(1)

print("--------------------------------------------")
print("End-to-End Login Flow Start")
print("--------------------------------------------")

sleep(1)
# Login with email-password
response, jwt_token = LOGIN().verify(
    mailID=sample_user["email"],
    password=sample_user["password"]
)

if response == LRC.LPR04:
    log.INFO(response)

sleep(1)

log.SUCCESS("End-to-End Login Flow Complete")
print("--------------------------------------------")