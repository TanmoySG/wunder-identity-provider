from time import sleep
from providers.authLib.authLib import AUTHLIB
from providers.registrationProvider.registration import REGISTER
from providers.authLib.standards.return_codes import RETURN_CODES as AUTHLIB_RC
from providers.mailer.mailer import MAILER
from providers.mailer.standards.return_codes import RETURN_CODES as MAILER_RC
from providers.mailer.content import CONTENT_FACTORY
from providers.registrationProvider.standards.return_codes import RETURN_CODES as RRC

from logsmith import log

# Setup Logsmith
log = log()
log.configure(ENV="DEV", logfile="logs", console_only=False)

sample_user = {
    "email": "tanmoysps@gmail.com",
    "name": "Joh Doe",
    "password": "123456"
}

response, otp = AUTHLIB().register(
    mailID=sample_user["email"],
    username=sample_user["name"],
    password=sample_user["password"]
)

log.INFO(response)

sleep(1)

if response == AUTHLIB_RC.ALR02:
    MAILER_1 = MAILER(mailer_mode=CONTENT_FACTORY.OTP_MAIL)
    MAILER_1.prepare_mail(payload=otp)
    response = MAILER_1.send_mail(sample_user["email"])

    log.INFO(response)


response, profile = AUTHLIB().verify(
    mailID=sample_user["email"],
    user_supplied_secret=otp
)

log.INFO(response)

sleep(2)

if response == AUTHLIB_RC.ALR14:
    response = REGISTER().register_verified_profile(verified_profile=profile)
    log.INFO(response)

    sleep(1)

    if response == RRC.RPR01:
        MAILER_2 =  MAILER(mailer_mode=CONTENT_FACTORY.VERIFIED_MAIL)
        MAILER_2.prepare_mail(payload=sample_user["email"])
        response = MAILER_2.send_mail(sample_user["email"])

        log.INFO(response)

log.SUCCESS("Process Complete")
