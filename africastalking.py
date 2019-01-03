import os
import africastalking


def main():
    africastalking.initialize(
        os.getenv('USERNAME', 'sandbox'), os.getenv('API_KEY', 'fake'))
    sms = africastalking.SMS

    def on_finish(error, data):
        if error is not None:
            raise error

        print('\nAsync Done with -> ' + str(data['SMSMessageData']['Message']))

    # Send SMS asynchronously
    sms.send('Hello Async', ['+256750461002'], callback=on_finish)
    print('Waiting for async result....')
    # Send SMS synchronously
    result = sms.send('Hello Sync Test', ['+256750461002'])
    print('\nSync Done with -> ' + result['SMSMessageData']['Message'])


if __name__ == "__main__":
    main()
