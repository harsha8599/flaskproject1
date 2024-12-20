from itsdangerous import URLSafeTimedSerializer
from key import salt
def encode(data):
    serializer=URLSafeTimedSerializer('manohar@2024')        #ffghgh
    return serializer.dumps(data,salt=salt)

def decode(data):
    serializer=URLSafeTimedSerializer('manohar@2024')        #123
    return serializer.loads(data,salt=salt)