from flask_restplus import Api
from run import APP
from .auth.views import Auth

API = Api(APP)
API.add_resource(Auth, '/auth')
