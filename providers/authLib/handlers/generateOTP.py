import hashlib, json, string, random, secrets

class OTP:

    def __init__(self):
        pass

    def generate(self, length):
        return ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits , k = length))