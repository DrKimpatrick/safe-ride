from functools import wraps
from flask import g, request
from ..models import User

# Restrics access to only logged in users
def authenticate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'Authorization' in request.headers:
            access_token = request.headers.get('Authorization')
            if access_token and len(access_token) != 0:
                # token = access_token.split(' ')[1]   # commented out code
                user = User.verify_auth_token(access_token)
                if user:
                    g.current_user = user
                    return func(*args, **kwargs)
                else:
                    return {
                        'error': 'Authorization failed try again'
                    }, 401
        return {
            'error': 'No Bearer token in Authorisation header'
        }, 401
    return wrapper