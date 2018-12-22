import os
from flask import request
from flask_restplus import Resource, reqparse
import re

class Auth(Resource):
    """ User signup and login """

    def post(self):
        """ signup """      
        return {"return": "return"}
