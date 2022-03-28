from handlers.generators import USERID, REGISTRATION_TIME, ACCESS_TOKEN
from handlers.profile import PROFILE

# USERID(), REGISTRATION_TIME(), 

token = ACCESS_TOKEN(length=128).generate()

print(token)

# print(
#     PROFILE().new_profile(
#         mailID="tanmoy",
#         userID=USERID(),
#         username="t",
#         password="trtt",
#         registration_timestamp=REGISTRATION_TIME(),
#         admin_access_token= token
#     )
# )

