# Using PyJWT - pip install pyjwt
# Documentation - https://pyjwt.readthedocs.io/en/latest/usage.html
import jwt

class JWT:

    def __init__(self, algorithm) -> None:
        self.algorithm = algorithm

    def get(self, payload, secret) -> str:
        self.token = jwt.encode(
            payload=payload,
            key=secret,
            algorithm=self.algorithm
        )

        return self.token
        

