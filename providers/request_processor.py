from logsmith import Logsmith

from providers.authLib.authLib import AUTHLIB
from providers.authLib.standards.return_codes import RETURN_CODES as AL_RC

from providers.login.login import LOGIN
from providers.login.standards.return_codes import RETURN_CODES as LG_RC

from providers.mailer.content import CONTENT_FACTORY
from providers.mailer.mailer import MAILER
from providers.mailer.standards.return_codes import RETURN_CODES as ML_RC

from providers.registration.registration import REGISTER
from providers.registration.standards.return_codes import RETURN_CODES as RG_RC

from providers.response_factory import RESPONSE_FACTORY

log = Logsmith({})
log.fetchConfigFromFile("configs/log.config.json")
log.prepareMonitor()

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
                    response=AL_RC.ALR02["details"],
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


    def account_verification_request_processor(self, request_data):

        response, profile = AUTHLIB().verify(
            mailID=request_data["email"],
            user_supplied_secret=request_data["otp"]
        )

        if response == AL_RC.ALR14:
            response = REGISTER().register_verified_profile(
                verified_profile=profile
            )

            if response == RG_RC.RPR01:
                VERIFICATION_MAILER = MAILER(mailer_mode=CONTENT_FACTORY.VERIFIED_MAIL)
                VERIFICATION_MAILER.prepare_mail(payload=request_data["email"])
                response = VERIFICATION_MAILER.send_mail(request_data["email"])

                if response == ML_RC.MLS01:
                    log.INFO(response["details"])
                    return RESPONSE_FACTORY().get(
                        status=response["response"],
                        response=RG_RC.RPR01["details"],
                        scopes={
                            AL_RC.ALR14["scope"]: AL_RC.ALR14["response"],
                            RG_RC.RPR01["scope"]: RG_RC.RPR01["response"],
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
                            RG_RC.RPR01["scope"]: RG_RC.RPR01["response"],
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
                        AL_RC.ALR14["scope"]: AL_RC.ALR14["response"],
                        response["scope"]: response["response"]
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


    def account_login_request_processor(self, request_data):
        
        response, payload = LOGIN().verify(
            mailID=request_data["email"],
            password=request_data["password"]
        )

        if response == LG_RC.LPR04:
            log.WARN(response["details"])
            return RESPONSE_FACTORY().get(
                status=response["response"],
                response=LG_RC.LPR04["details"],
                scopes={
                    LG_RC.LPR04["scope"]: LG_RC.LPR04["response"]
                },
                payload=payload
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