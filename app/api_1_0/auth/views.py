from flask import request, jsonify
import requests
from app import db
from ...models import User, Login as UserLoign
from ...api_1_0 import API_BP
from .utils import is_str_empty, check_auth
from ..send_email import send_email


@API_BP.route('/auth/signup', methods=['POST'])
def register():
    """ Creates new user account """

    errors = {}
    signup = 'signup'

    # This populates the error dict if any field is missing
    check_auth(errors, signup)

    # This returns an error if no data is passed
    if check_auth(errors, signup):
        return check_auth(errors, signup)

    if errors:
        return jsonify({
            'errors': errors
        }), 400

    # We are now sure that all information is provided
    data = request.json['credentials']
    email = data['email']
    password = data['password']
    callback_url = data['callback_url']

    user = User.query.filter_by(email=email).first()
    if user:
        errors['email'] = 'This email is already in use'
        return jsonify({
            'errors': errors
        }), 400

    # create and login the user automatically
    new_user = User(email=email, password=password)
    db.session.add(new_user)
    db.session.commit()

    # First save the user before generating token
    token = new_user.generate_auth_token(10000)

    # Don't auto manatically login the user
    # User should first verify their account to login

    # After successfull signup
    # Send verication email
    send_email(email, token, callback_url)

    return jsonify({
        'message': 'You are successfully signed up to Safe-ride \n'\
        'A verification link has been sent by mail, click it to verify you account'
    }), 201


@API_BP.route('/auth/login', methods=['POST'])
def login():

    errors = {}
    login = 'login'

    # This populates the error dict if any field is missing
    check_auth(errors, login)

    # This returns an error if no data is passed
    if check_auth(errors, login):
        return check_auth(errors, login)

    if errors:
        return jsonify({
            'errors': errors
        }), 400

    # We are now sure that all information is provided
    data = request.json['credentials']
    email = data['email']
    password = data['password']

    user = User.query.filter_by(email=email).first()

    if user is not None and user.verify_password(password):
        token = user.generate_auth_token(10000)
        ip = request.remote_addr
        user_login = UserLoign(user_id=user.id, ip_address=ip)
        db.session.add(user_login)
        db.session.commit()
        return jsonify({
            'token': token,
            'email': user.email,
            'id':  user.id
        }), 200

    return jsonify({
        'errors': {
            'form': 'Wrong email or password'
        }
    }), 401
