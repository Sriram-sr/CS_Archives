import jwt
from lavazza_cfds_mobile_app_server_macros import *

public_key = open(PUBLIC_KEY).read()

def verify_token(token_id):
    try:
        jwt.decode(token_id, public_key, issuer=ISSUER, algorithms=['RS256'])
        return "verified"
    except Exception as token_error:
        return token_error