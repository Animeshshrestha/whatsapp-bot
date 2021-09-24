from flask import Flask, jsonify, request

from .twillo import twillo_instance

app = Flask(__name__)

@app.route('/whatsapp/webhook', methods=['GET','POST'])
def whatsapp_webhook():

    if request.method == "GET":
        msg = twillo_instance.send_message(
            body = "Hello World",
            to_no = "9779861602256"
        )
        return msg

    if request.method == "POST":

        msg = request.form.get('Body')
        resp = twillo_instance.reply_message(msg)
        return resp

        # Create reply
        # resp = MessagingResponse()
        # resp.message("You said: {}".format(msg))
