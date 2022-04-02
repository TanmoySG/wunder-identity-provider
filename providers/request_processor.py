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

log = log()
log.configure(ENV="DEV", logfile="logs", console_only=True)

class REQUEST_PROCESSOR:
    def __init__(self) -> None:
        pass

    def new_registration_request_processor(self, request_data):

        response, otp = AUTHLIB().register(
            mailID=request_data["email"],
            username=request_data["name"],
            password=request_data["password"]
        )

        if response == AL_RC.ALR02:
            REGISTRATION_MAILER = MAILER(mailer_mode=CONTENT_FACTORY.OTP_MAIL)
            REGISTRATION_MAILER.prepare_mail(payload=otp)
            response = REGISTRATION_MAILER.send_mail(request_data["email"])

            if response == ML_RC.MLS01:
                log.INFO(response["details"])
                return RESPONSE_FACTORY().get(
                    status=response["response"],
                    response=response["details"],
                    scopes={
                        AL_RC.ALR02["scope"]: AL_RC.ALR02["response"],
                        ML_RC.MLS01["scope"]: ML_RC.MLS01["response"]
                    },
                    payload={}
                )
            else:
                log.WARN(response["details"])
                return RESPONSE_FACTORY().get(
                    status=response["response"],
                    response=response["details"],
                    scopes={
                        AL_RC.ALR02["scope"]: AL_RC.ALR02["response"],
                        ML_RC.MLS02["scope"]: ML_RC.MLS02["response"]
                    },
                    payload={}
                )
        else:
            log.WARN(response["details"])
            return RESPONSE_FACTORY().get(
                status=response["response"],
                response=response["details"],
                scopes={
                    response["scope"]: response["response"]
                },
                payload={}
            )

