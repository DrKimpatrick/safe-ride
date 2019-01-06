import os
from flask import request, make_response
from flask_restplus import Resource, reqparse
import re


def respond(menu_text):
    response = make_response(menu_text, 200)
    response.headers['Content-Type'] = "text/plain"
    return response


class Auth(Resource):
    """ User signup and login """

    def post(self):
        """ signup """

        # GET values from the AT's POST request
        session_id = request.values.get("sessionId", None)
        phone_number = request.values.get("phoneNumber", None)

        text_string = request.values.get("text", "default")
        text_array = text_string.split("*")
        text = text_array[len(text_array) - 1]
        text_1 = text_string

        # user_response = text_array[len(text_array) - 1]

        full_response = "session_id: {} phone_number: {} text_string: {}".format(session_id, phone_number, text_string)

        personal_info = [{"mobile_phone": '0750461002', "pin": "15712", "name": "Patrick", "balance": 300000 },
                        {"mobile_phone": '+256782579882', "pin": "15712", "name": "Lukwata", "balance": 2300000 },
                        {"mobile_phone": '+256750461002', "pin": "15712", "name": "Patrick", "balance": 300000 }
                        ]

        response = ''

        def check_phone():
            for data in personal_info:
                if data['mobile_phone'] == str(phone_number):
                    return {"pin": data['pin'], "name": data['name'], "balance": data['balance']}
            else:
                return False

        if text_1 == '':
            
            response_true = "CON Save more and get an instant \n" \
                    " loan of up to 2M UGX on \n Centemobile" \
                    "Select Options: \n" \
                    "1. Centemobile \n" \
                    "2. Agent Banking"

            response_false = "END To use Centemobile \n" \
                            "please visit any Centenary bank \n" \
                            "branch and complete your registration"
            
            response = response_true if check_phone() else response_false

        elif text_1 == '1':
            response = "CON Dear {}, You can now get \n "\
                        "an instant loan of upto 2M UGX \n" \
                        "on Centemobile. Enter PIN to \n" \
                        "continue.".format(check_phone()['name'])
        elif text_1 == '1*{}'.format(check_phone()['pin']):
            response = "CON Reply with \n" \
                        "1. Account Balance \n" \
                        "2. Centemobile loans \n" \
                        "3. Mini Statement \n" \
                        "4. Funds Transfer \n" \
                        "5. Airtime"
        # elif text_1 != '1*{}'.format(check_phone()['pin']) and text_1 != '':
        #     response = "END Incorrect pin, please try again text: {}".format(text_1)

        elif text_1 == '1*{}*1'.format(check_phone()['pin']):
            response = "CON Select Bank: \n" \
                        "1 Centenary Bank/7355355353"
        
        elif text_1 == '1*{}*1*1'.format(check_phone()['pin']):
            response = "END Actual Balance UGX{} CR" \
                        "Available Balance UGX {} \n" \
                        "CR \n"\
                        "0. Back".format(check_phone()['balance'], check_phone()['balance'])
        else:
            response = "END Incorect input. Please try again"
        
        return respond(response)
