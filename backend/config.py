import os
from datetime import timedelta
from dotenv import load_dotenv

class TestConfig:
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    MONGO_URI = "mongodb://localhost:27017/mvp_test"
    SECRET_KEY = "2934948fn394fnqp4ifqp394fSRHF8EFH9WEFn9"
    JWT_ALGORITHM="RS256"
    JWT_PRIVATE_KEY='''-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC70EAeUSK59eF0
43GxviHLy8PunypLTEL2UqywWTQo1y/6UiaYDQFOVkf7rHqX7J9p67BOnFf8c/4n
bYZcKdGEAYMAQVKpFaoBcL27tpMSHZrBeuv5Eppk/v/JMdF/VOQMKkAZ4eqwiMXB
EVFiGhCJsu6PffzwNjQbZYdwInW7oJoGDGWhbCK5iw3OOW43IDyzIKqSe8lkHlyQ
lIawf5cTdbdIKDfnlj0brJVUqnEiXMv62duj8CGeVPsvRFc+TBGL8st/iLKwXD5P
LowSh6BAGIFvND+WszmoTJm1dhBExyxiNg3udI+ICHg9RPD4dmZPzo281mWv9js0
Qg0ml/KJAgMBAAECggEADTm5+iiOgHffG4MUs4aHDLnZn0kYClthb8UcogJ2GNYm
a8MzMovf5qtOwFtB+sbP5v6Q2MhLrdxhLleZGY5cUaZlmjP/ZSbAZP+SbNCLhMAO
8Mb+LPjxZGFMk9dtQEEzGeQzxV7STwIiotjcWUMqnPe7suEVWbkHbFJ2+h+DGOY0
X3M5Puf10SX227Dazk+oJ4ULJ9IW3vkENeeY+U0LIYEY25mn52PyiCkgNeUOfwIT
1tgQYgaWQEhQlx0a4w0HInztRIGlLwW1Kv2wyYNIF65kvQhQ/9ylzm2QzErosfPY
anPO068KB9d0LUuCyGVrTArd0DyMdbLpAD6qOkDTDQKBgQDqOBENv/P6SYYG7VZz
//s7BhBwigxAKMm609fY/YxDC5wggw13gFdbCf0HGhSZw5RqpuWmV3JBEKXXg1Gb
COjTiG94L9x6OZ31LzyAPnAc0j0+0Wysm/vnl5qVMaO5pNob+whzk2fr27mPO80J
qX1CDgtJwu7sXk9P/5u//2/lhwKBgQDNR25L8nzVOYDk1pW720Iom2mb5E9vbyWj
LxLxb2KwzcJFWtk2Rvg3i1pxKScLHxHjW2R4MTOV86oZOCQax0gpdfJke7jGNiAS
K2FjrwiAqFoLV+H6CP3mAMEmFTpnN+MrdN38dQRyCGtPeaLx6J4TJWhpW64T9YyW
KNpOp7xrbwKBgQCFrfxlyaIZvy8E8x890+NzO7HUWaZGVEFXJaPzkDsm5RB2KfZc
t16kcl39WLBbVpp2CM3YE979LeBJ0gSYpQwl96APi9md1RbHou84Dur0ODaGjQcm
uVycQRYUgyF8So/GGpAnTwGoR19wVeRf2GHKerOMpPqy490GvtAJVGRsLwKBgEfP
aygqRb0ZhpuG7Y5v3y7xXvpn3dnvmc0CFLBc9LtA32r/oui33vEfUJ4xdTUQw2Mz
f2wEWjVkreZwm0C64eWPGyJHnZXJLWLtxf3nJyRKwGUjcyvSpW8maGr4FhwxksiK
83TzQoDZrSB6PqQ9ab7s4R+qMLVOusV0uRm219UFAoGABgOA9LKGf+G31sc0cDo4
ULl3i9aEdihDn7hQ8tRd/xlqQlqgZG5FpCxMIQQ0LtUDKIgsLpgaeHWdA005YbFi
qlrgmc2UOPAZHBj13jZcL9pl+gOSTj1x+7lUQPL/ucxzfiO7QGMXIjlOQUtxK2AO
DD4nS+BQ68CPPzwuuaM/ZJE=
-----END PRIVATE KEY-----'''
    JWT_PUBLIC_KEY='''-----BEGIN RSA PUBLIC KEY-----
MIIBCgKCAQEAu9BAHlEiufXhdONxsb4hy8vD7p8qS0xC9lKssFk0KNcv+lImmA0B
TlZH+6x6l+yfaeuwTpxX/HP+J22GXCnRhAGDAEFSqRWqAXC9u7aTEh2awXrr+RKa
ZP7/yTHRf1TkDCpAGeHqsIjFwRFRYhoQibLuj3388DY0G2WHcCJ1u6CaBgxloWwi
uYsNzjluNyA8syCqknvJZB5ckJSGsH+XE3W3SCg355Y9G6yVVKpxIlzL+tnbo/Ah
nlT7L0RXPkwRi/LLf4iysFw+Ty6MEoegQBiBbzQ/lrM5qEyZtXYQRMcsYjYN7nSP
iAh4PUTw+HZmT86NvNZlr/Y7NEINJpfyiQIDAQAB
-----END RSA PUBLIC KEY-----'''
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=1) # you probably want to change this to a short time
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)
    JWT_REGISTRATION_TOKEN_EXPIRES = timedelta(seconds=2)
    JWT_PASSWORD_TOKEN_EXPIRES = timedelta(seconds=2)
    FRONT_END_URL = 'http://localhost:3000'



class DevConfig:
    MONGO_URI = "mongodb://localhost:27017/flask" # mongodb standard port, and flask is the name of the database

    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    MONGO_URI = "mongodb://localhost:27017/mvp_dev"
    SECRET_KEY = "293"
    JWT_ALGORITHM="RS256"
    JWT_PRIVATE_KEY='''-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC70EAeUSK59eF0
43GxviHLy8PunypLTEL2UqywWTQo1y/6UiaYDQFOVkf7rHqX7J9p67BOnFf8c/4n
bYZcKdGEAYMAQVKpFaoBcL27tpMSHZrBeuv5Eppk/v/JMdF/VOQMKkAZ4eqwiMXB
EVFiGhCJsu6PffzwNjQbZYdwInW7oJoGDGWhbCK5iw3OOW43IDyzIKqSe8lkHlyQ
lIawf5cTdbdIKDfnlj0brJVUqnEiXMv62duj8CGeVPsvRFc+TBGL8st/iLKwXD5P
LowSh6BAGIFvND+WszmoTJm1dhBExyxiNg3udI+ICHg9RPD4dmZPzo281mWv9js0
Qg0ml/KJAgMBAAECggEADTm5+iiOgHffG4MUs4aHDLnZn0kYClthb8UcogJ2GNYm
a8MzMovf5qtOwFtB+sbP5v6Q2MhLrdxhLleZGY5cUaZlmjP/ZSbAZP+SbNCLhMAO
8Mb+LPjxZGFMk9dtQEEzGeQzxV7STwIiotjcWUMqnPe7suEVWbkHbFJ2+h+DGOY0
X3M5Puf10SX227Dazk+oJ4ULJ9IW3vkENeeY+U0LIYEY25mn52PyiCkgNeUOfwIT
1tgQYgaWQEhQlx0a4w0HInztRIGlLwW1Kv2wyYNIF65kvQhQ/9ylzm2QzErosfPY
anPO068KB9d0LUuCyGVrTArd0DyMdbLpAD6qOkDTDQKBgQDqOBENv/P6SYYG7VZz
//s7BhBwigxAKMm609fY/YxDC5wggw13gFdbCf0HGhSZw5RqpuWmV3JBEKXXg1Gb
COjTiG94L9x6OZ31LzyAPnAc0j0+0Wysm/vnl5qVMaO5pNob+whzk2fr27mPO80J
qX1CDgtJwu7sXk9P/5u//2/lhwKBgQDNR25L8nzVOYDk1pW720Iom2mb5E9vbyWj
LxLxb2KwzcJFWtk2Rvg3i1pxKScLHxHjW2R4MTOV86oZOCQax0gpdfJke7jGNiAS
K2FjrwiAqFoLV+H6CP3mAMEmFTpnN+MrdN38dQRyCGtPeaLx6J4TJWhpW64T9YyW
KNpOp7xrbwKBgQCFrfxlyaIZvy8E8x890+NzO7HUWaZGVEFXJaPzkDsm5RB2KfZc
t16kcl39WLBbVpp2CM3YE979LeBJ0gSYpQwl96APi9md1RbHou84Dur0ODaGjQcm
uVycQRYUgyF8So/GGpAnTwGoR19wVeRf2GHKerOMpPqy490GvtAJVGRsLwKBgEfP
aygqRb0ZhpuG7Y5v3y7xXvpn3dnvmc0CFLBc9LtA32r/oui33vEfUJ4xdTUQw2Mz
f2wEWjVkreZwm0C64eWPGyJHnZXJLWLtxf3nJyRKwGUjcyvSpW8maGr4FhwxksiK
83TzQoDZrSB6PqQ9ab7s4R+qMLVOusV0uRm219UFAoGABgOA9LKGf+G31sc0cDo4
ULl3i9aEdihDn7hQ8tRd/xlqQlqgZG5FpCxMIQQ0LtUDKIgsLpgaeHWdA005YbFi
qlrgmc2UOPAZHBj13jZcL9pl+gOSTj1x+7lUQPL/ucxzfiO7QGMXIjlOQUtxK2AO
DD4nS+BQ68CPPzwuuaM/ZJE=
-----END PRIVATE KEY-----'''
    JWT_PUBLIC_KEY='''-----BEGIN RSA PUBLIC KEY-----
MIIBCgKCAQEAu9BAHlEiufXhdONxsb4hy8vD7p8qS0xC9lKssFk0KNcv+lImmA0B
TlZH+6x6l+yfaeuwTpxX/HP+J22GXCnRhAGDAEFSqRWqAXC9u7aTEh2awXrr+RKa
ZP7/yTHRf1TkDCpAGeHqsIjFwRFRYhoQibLuj3388DY0G2WHcCJ1u6CaBgxloWwi
uYsNzjluNyA8syCqknvJZB5ckJSGsH+XE3W3SCg355Y9G6yVVKpxIlzL+tnbo/Ah
nlT7L0RXPkwRi/LLf4iysFw+Ty6MEoegQBiBbzQ/lrM5qEyZtXYQRMcsYjYN7nSP
iAh4PUTw+HZmT86NvNZlr/Y7NEINJpfyiQIDAQAB
-----END RSA PUBLIC KEY-----'''
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=1)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)
    JWT_REGISTRATION_TOKEN_EXPIRES = timedelta(days=1)
    JWT_PASSWORD_TOKEN_EXPIRES = timedelta(minutes=15)
    FRONT_END_URL = 'http://localhost:3000'

class ProdConfig:
    load_dotenv()
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    MONGO_URI = os.getenv('MONGO_URI')
    SECRET_KEY = os.getenv('SECRET_KEY')
    JWT_ALGORITHM="RS256"
    JWT_PRIVATE_KEY=os.getenv('JWT_PRIVATE_KEY')
    JWT_PUBLIC_KEY=os.getenv('JWT_PUBLIC_KEY')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=1)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)
    SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')
    