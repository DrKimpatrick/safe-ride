import os
from flask import request
from flask_restplus import Resource, reqparse
import re

class Auth(Resource):
    """ User signup and login """

    def post(self):
        """ signup """
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int, required=True,
                            help='xxxxxxxxxx')  
        args = parser.parse_args()

        error = {}  
        request_data = request.json
        if "email" not in request_data:
            error['email'] = "Email is required"
        # elif not isinstance(request_data['email'], str):
        #     error['email'] = "Invalid email formatccc"
        elif not re.match(r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+$)", str(request_data['email'])):
            error['email'] = "Invalid email format"
        if "username" not in request_data:
            error['username'] = "username is required"
        else:
            if not isinstance(request_data['username'], str):
                error['username'] = "username should be of type string"
            elif len(request_data['username']) < 6 or len(request_data['username']) > 10:
                error['username'] = "Username should be atleast 6 characters long and atmost 10 characters long"
        if "password" not in request_data:
            error['password'] = "Password is required"
        if len(request_data['password']) < 8 or re.search(r"(/[a-zA-Z{1,9}]/)", request_data['password']):
            error['password'] = "Password should be alphanumeric with at least 8 characters"

        # if len(request_data['password']) < 8 or request_data['password'].search(r"/[a-zA-Z]/") == -1):
            
        return {"error": error}