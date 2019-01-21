import sendgrid
import os
from sendgrid.helpers.mail import *


def send_email(to_email, token, callback_url):
    """ Sending emails with sendgrid """

    sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
    from_email = Email("dr.kimanje2patrick2@gmail.com")
    to_email = Email(to_email)
    subject = "Email verification"
    body = 'Safe-ride account activation. \n' \
            'Hey there, Thank you for expressing interest in Safe-ride. \n' \
            'Follow the link to activate your account \n' \
            '{}/{}'.format(callback_url, token)

    content = Content("text/plain", body)
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
