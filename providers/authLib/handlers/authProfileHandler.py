from generators import OTP, TIMESTAMP

_OTP = OTP().generate(6)

print(_OTP)

_CURRENT_TIMESTAMP = TIMESTAMP().generate()

print(_CURRENT_TIMESTAMP[0])