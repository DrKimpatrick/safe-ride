"""
This module contains data used by other test modules
"""
import unittest
import os
from app import create_app, db

    
class BaseTest(unittest.TestCase):
    """
    This class contains data required for testing by test classes.
    """
    APP = create_app(os.getenv('APP_SETTINGS') or 'testing')

    def setUp(self):
        # Create tables for the test database
        db.create_all(app=self.APP)
        
        self.app = self.APP.test_client()

        self.email = "dr.kimpat@gmail.com"
        self.password = "Kpassword12"

        # Signup ****************************

        # The right user data
        self.user_data_right = {"credentials": {
            "email": self.email,
            "password": self.password
        }}

        # No key credentials provided
        self.user_data_no_credentials_key = {"cred": {}}

        # user data with email and password missing
        self.user_data_missing = {"credentials": {
            "email": "",
            "password": ""
        }}

        # user data with invalid email format
        self.user_data_ivalid_email = {"credentials": {
            "email": "email@gmail",
            "password": self.password
        }}

        # user data with invalid password
        self.user_data_invalid_pass = {"credentials": {
            "email": self.email,
            "password": "password"
        }}

        # Signup responses: Below is a list of common responses

        # Missing all fields
        self.missing_all_fields_error = {'errors': {'email': 'This field is required',
                                                    'password': 'This field is required'}}

        # When invalid email is supplied
        self.invalid_email_error = {'errors': {
            'email': 'Enter a valid email address.'}}

        # When invalid password is supplied
        self.invalid_password_error = {"errors": {
            "password": "Password should be alphanumeric with at least 8 characters"
        }}

        # When no user data is provided
        self.no_user_data_provided = {
            'errors': 'Credentials are required to login'}

        # When key credentials is not provided
        self.user_data_no_credentials_error = {'errors': {
            'credentials': 'Credentials are required to login'}}

        # Signing up with an already existing email
        self.user_email_already_existing_error = {'errors': {
            'email': 'This email is already in use'
        }}

        # Login ********************************

        # self.user_data_right | used when creating a user
        # The same data is used for a successfull login

        # Mis-matching data for the created user
        self.user_data_not_matching = {"credentials": {
            "email": self.email,
            "password": 'password'
        }}

        # Login responses
        self.invalid_login = {'errors': {'form': 'Wrong email or password'}}

    def tearDown(self):
        db.drop_all(app=self.APP)
