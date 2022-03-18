from generators import OTP, TIMESTAMP, UUID

_OTP = OTP().generate(length = 6)

print(_OTP)

_CURRENT_TIMESTAMP = TIMESTAMP().generate(timeframe = 120)

print(_CURRENT_TIMESTAMP[0])

_UUID = UUID().generate()
print(_UUID)