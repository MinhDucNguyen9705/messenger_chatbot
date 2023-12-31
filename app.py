from flask import Flask, request
import requests
 
app = Flask(__name__)
 
# This is page access token that you get from facebook developer console.
PAGE_ACCESS_TOKEN = 'EAALhqZA10PZCwBO3p1Bgdkk9guwDFHM6AZC8sKZCM4XYY8MYDIiAimqoJSZBEs6Nmih7Cjcb04INS1vVgRqiVDSdmVK4pMk6KF87xIPUWQlVTcn4JRwL8vsBipSgKjpQgZAXBcPxGN0yvRnhNzrxljIbwls52yhnJOtgc0JPASVxgAcLGo10MZC1tIx7WSUMJYe2k1p'
# This is API key for facebook messenger.
API = "https://graph.facebook.com/LATEST-API-VERSION/me/messages?access_token="+PAGE_ACCESS_TOKEN

def message_process(text):
    text = text.lower()
    if text=='hi':
        return 'Hello'
    elif text=='how are you?':
        return 'I\'m good'
    else:
        return 'Error! Try again later'

@app.route("/", methods=['GET'])
def fbverify():
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token")== "minhduc321123":
            return "Verification token missmatch", 403
        return request.args['hub.challenge'], 200
    return "Hello world", 200

@app.route("/", methods=['POST'])
def fbwebhook():
    data = request.json
    print(data)
    try:
        message = data['entry'][0]['messaging'][0]['message']
        sender_id = data['entry'][0]['messaging'][0]['sender']['id']
        print(message)
        print(sender_id)
        text = message_process(message['text'])
        print(text)
        request_body = {
            "recipient": {
                "id": sender_id
            },
            "message": {
                "text": text
            }
        }
        response = requests.post(API, json=request_body).json()
        print(response)
        message_send(sender_id, text)
        return 'Message received'
    except:
        request_body = {
                "recipient": {
                    "id": sender_id
                },
                "message": {
                    "text": "Error!"
                }
            }
        response = requests.post(API, json=request_body).json()
        message_send(sender_id, 'Error!')
        return response
from pymessenger.bot import Bot
bot = Bot(PAGE_ACCESS_TOKEN)

def message_send(recipient_id, response):
	bot.send_text_message(recipient_id, response)
	return "success"

if __name__ =='__main__':
    app.run()