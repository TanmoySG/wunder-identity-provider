class PROFILE:

    def __init__(self) -> None:
        pass

    def new_profile(self, mailID, userID, username, password, registration_timestamp, admin_access_token):
        self.profile = {
            "email": mailID,
            "user_uID": userID,
            "name": username,
            "password": password,
            "admin_access_token": admin_access_token,
            "registration_timestamp": registration_timestamp,
            "services": {}
        }

        return self.profile
