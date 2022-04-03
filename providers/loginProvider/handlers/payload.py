class PAYLOAD:

    def get(self, profile) -> dict:
        self.payload = {
            "usr": profile["email"],
            "uid": profile["user_uID"],
            "aat": profile["admin_access_token"]
        }
        return self.payload
