from .base_tests import BaseTest
import json

BASE_URL = '/api/v1'
CONTENT_TYPE = 'application/json'


class TestSignUp(BaseTest):
    """ Class contains test suites for testing 
        : signup
    """

    def test_signup_valid_data(self):
        """ Provide valid data 
            : expect new user to be created
        """
        response = self.app.post('{}/auth/signup'.format(BASE_URL),
                                 data=json.dumps(self.user_data_right),
                                 content_type=CONTENT_TYPE)

        self.assertEqual(response.status_code, 201)

    def test_signup_missing_data(self):
        """ Missing email and password
            : expect an error message
        """

        response = self.app.post('{}/auth/signup'.format(BASE_URL),
                                 data=json.dumps(self.user_data_missing),
                                 content_type=CONTENT_TYPE)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, self.missing_all_fields_error)

    def test_signup_invalid_email(self):
        """ Invalid email supplied """

        response = self.app.post('{}/auth/signup'.format(BASE_URL),
                                 data=json.dumps(self.user_data_ivalid_email),
                                 content_type=CONTENT_TYPE)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, self.invalid_email_error)

    def test_signup_invalid_password(self):
        """ Invalid password supplied """

        response = self.app.post('{}/auth/signup'.format(BASE_URL),
                                 data=json.dumps(self.user_data_invalid_pass),
                                 content_type=CONTENT_TYPE)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, self.invalid_password_error)

    def test_signup_no_data_provided(self):
        """ When user has not provided credentials in the json body
            : expect to raise an error
        """

        response = self.app.post('{}/auth/signup'.format(BASE_URL),
                                 content_type=CONTENT_TYPE)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, self.no_user_data_provided)

    def test_signup_no_credentials_key(self):
        """ When user has not provided any data
            : expect to raise an error
        """

        response = self.app.post('{}/auth/signup'.format(BASE_URL),
                                 data=json.dumps(
                                    self.user_data_no_credentials_key),
                                 content_type=CONTENT_TYPE)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, self.user_data_no_credentials_error)


class TestLogin(BaseTest):
    """ Class contains test suites for testing 
        : login
    """

    def create_user(self):
        # Register default user
        self.app.post('{}/auth/signup'.format(BASE_URL),
                      data=json.dumps(self.user_data_right),
                      content_type=CONTENT_TYPE)

    def test_login_valid_data(self):
        """ Provide valid data | create and login user
            : expect new user to be login user
        """
        # call create user function
        self.create_user()

        # login user
        response = self.app.post('{}/auth/login'.format(BASE_URL),
                                 data=json.dumps(self.user_data_right),
                                 content_type=CONTENT_TYPE)

        self.assertEqual(response.status_code, 200)

    def test_login_data_not_matching(self):
        """ Provide data that does not match
            : expect to raise an error
        """
        # call create user function
        self.create_user()

        # login user
        response = self.app.post('{}/auth/login'.format(BASE_URL),
                                 data=json.dumps(self.user_data_not_matching),
                                 content_type=CONTENT_TYPE)

        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json, self.invalid_login)

    def test_login_data_missing(self):
        """ Provide data that does not match
            : expect to raise an error
        """
        # call create user function
        self.create_user()

        # login user
        response = self.app.post('{}/auth/login'.format(BASE_URL),
                                 data=json.dumps(self.user_data_missing),
                                 content_type=CONTENT_TYPE)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, self.missing_all_fields_error)

    def test_login_no_data_provided(self):
        """ When user has not provided any data
            : expect to raise an error
        """
        # call create user function
        self.create_user()

        # login user
        response = self.app.post('{}/auth/login'.format(BASE_URL),
                                 content_type=CONTENT_TYPE)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, self.no_user_data_provided)
