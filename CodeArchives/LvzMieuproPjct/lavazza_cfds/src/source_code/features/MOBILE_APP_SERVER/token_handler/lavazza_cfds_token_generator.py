import jwt
import datetime
from lavazza_cfds_mobile_app_server_macros import *

private_key = open(PRIVATE_KEY).read()

token = jwt.encode({"exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=120), "iss": ISSUER}, private_key, algorithm='RS256').decode('utf-8')

print(token)

