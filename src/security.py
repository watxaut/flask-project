from werkzeug.security import safe_str_cmp
from src.user import User

users = [
    User(1, "Joan", "pwd")
]

username_mapping = {u.username: u for u in users}

userid_mapping = {u.id: u for u in users}


def authenticate(name, pwd):
    user = username_mapping.get(name, None)
    if user is not None and safe_str_cmp(user.password, pwd):
        return user


# unique to flask-jwt
# Payload is the content of the jwt token
def identity(payload):
    user_id = payload["identity"]
    return userid_mapping.get(user_id, None)
