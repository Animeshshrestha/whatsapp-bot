from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse


class TwilloWhatsApp:

    def __init__(self):
        self.account_sid = 'ACc8803cd403a55c8ec2c5ecb6b88d3b54'
        self.auth_token = '1d2fe35e371af4cd892047794be301e6'

    @property
    def create_client_instance(self):
        return Client(self.account_sid, self.auth_token)
    
    def send_message(self, **kwargs):

        body = kwargs.get('body')
        from_no = kwargs.get('from_no','+14155238886')
        to_no = kwargs.get('to_no')

        message = self.create_client_instance.messages.create(
                              body=body,
                              from_='whatsapp:{}'.format(from_no),
                              to='whatsapp:+{}'.format(to_no)
                          )
        return message._properties
    
    def reply_message(self, message):

        resp = MessagingResponse()
        resp.message("Message Sent was {}".format(message))
        return str(resp)

twillo_instance = TwilloWhatsApp()
