from flask_restplus import Api
from run import APP
from .auth.views import Environment

API = Api(APP)
API.add_resource(Environment, '/environment')
