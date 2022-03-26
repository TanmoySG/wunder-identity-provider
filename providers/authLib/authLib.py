from time import sleep
from handlers.requestHandler import AUTH_REQUEST
from handlers.maintenanceHandler import MAINTENANCE

MAINTENANCE().short_term_purge()

# Eg - In-time verification - should successfully verify account
email_id = "random1@gmail.com"
name="Jane Doe"
pw="123454"

_otp=AUTH_REQUEST().register(mailID=email_id, name=name, password=pw)

sleep(5)

returrn_val = AUTH_REQUEST().verify(verification_mail=email_id, verification_OTP=_otp)

#placeholder code
print(returrn_val)

# Eg - Out-of timeframe/window verification - Should Fail
email_id = "random2@gmail.com"
name="Jane Doe"
pw="123454"

_otp=AUTH_REQUEST().register(mailID=email_id, name=name, password=pw)
sleep(5) # Verification window 10s
returrn_val = AUTH_REQUEST().verify(verification_mail=email_id, verification_OTP=_otp)

#placeholder code
print(returrn_val)