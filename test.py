from providers.authLib.authLib import AUTHLIB

resposne, otp = AUTHLIB().register(
    mailID="tanmoysps@gmail.com",
    username="tanmoy",
    password="1234567789"
)

print(resposne, otp)