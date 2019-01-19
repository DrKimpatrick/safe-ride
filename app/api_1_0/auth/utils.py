from flask import request, jsonify
import re


def is_str_empty(param):
    """ Checks if param is empty """
    return not param.strip(' ')


def email_validation(email):
    """ Checks for validity of user email 
        valid email: example@gmail.com
    """

    if not re.match(r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+$)", email):
        return 'Enter a valid email address.'


def pass_validation(password, action):
    """ Password should be alphanumeric
        : atleast one letter or number
        at least 8 characters long
    """
    if action == 'signup':
        if not re.match('^(?=.*[0-9]$)(?=.*[a-zA-Z])', password) or len(password) < 8:
            return "Password should be alphanumeric with at least 8 characters"


def check_auth(errors, action):
    """ Function checks whether all required params
        : are provided
        Errors are added to the errors dictionary
        Terminate if no data is passed
    """
    # check if any data is supplied
    if not request.data:
        return jsonify({
            'errors': 'Credentials are required to login'
        }), 400

    if 'credentials' not in request.json:
        errors['credentials'] = 'Credentials are required to login'
    else:
        data = request.json['credentials']

        if 'email' not in data:
            errors['email'] = 'Email field is required'
        else:
            email = data['email']
            if is_str_empty(email):
                errors['email'] = 'This field is required'
            elif email_validation(email):
                errors['email'] = email_validation(email)

        if 'password' in data:
            password = data['password']
            if is_str_empty(password):
                errors['password'] = 'This field is required'
            elif pass_validation(password, action):
                errors['password'] = pass_validation(password, action)
        else:
            errors['password'] = 'Password field is required'
