import os
from flask import request
from flask_restplus import Resource, reqparse
import re


class Auth(Resource):
    """ User signup and login """

    def post(self):
        """ signup """

        my_list = ['phoneNumber', 'text', 'sessionId', 'serviceCode']
        errors = []
        for param in my_list:
            if (not request.json or param not in request.json):
                errors.append("{} is required".format(param))

        if errors:
            return {"error": errors}

        final = []
        for param in my_list:
            key = param
            param = request.json[param]
            final.append({key: param})

        text = final[1]['text']

        response = ''
        if text == '':
            # This is the first request. Note how we start the response with CON
            response = "CON What would you want to check \n"\
                "1. My Account \n" \
                "2. My phone number"

        elif text == '1':
            # Business logic for first level response
            response = "CON Choose account information you want to view \n" \
                "1. Account number \n" \
                "2. Account balance"

        elif text == '2':
            # Business logic for first level response
            # This is a terminal request. Note how we start the response with END
            response = "END Your phone number is " + \
                str(final[0]['phoneNumber'])

        elif text == '1*1':
            # This is a second level response where the user selected 1 in the first instance
            account_number = "ACC1001"

            # This is a terminal request. Note how we start the response with END
            response = "END Your account number is " + account_number

        elif text == '1*2':
            # This is a second level response where the user selected 1 in the first instance
            balance = "KES 10,000"

            # This is a terminal request. Note how we start the response with END
            response = "END Your balance is " + balance

        # return {'My_text': final}
        # header('Content-type: text/plain')
        return response
