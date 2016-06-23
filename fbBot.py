from flask import Flask, request
import requests
import json

app = Flask(__name__)

ACCESS_TOKEN = "EAADZBvOKZA9vsBAPDw2GQi7b1u0eS2OPDOrtiBdCowTwnmw9QdZByLm7KIsCrBm7QbY1aFbFZCQbMaFcZC6DDgJoPkT9niucr5bEAZBKYde2qH05oGQbScxaEwdFNH8SG53AQJ0XO35tmq6mBSy4RkQMth0MVG4bcgzH9W6jIyogZDZD"
VERIFY_TOKEN = "secret"

def reply(recipient_id, message_text):
    params = {
        "access_token" : "EAADZBvOKZA9vsBAPDw2GQi7b1u0eS2OPDOrtiBdCowTwnmw9QdZByLm7KIsCrBm7QbY1aFbFZCQbMaFcZC6DDgJoPkT9niucr5bEAZBKYde2qH05oGQbScxaEwdFNH8SG53AQJ0XO35tmq6mBSy4RkQMth0MVG4bcgzH9W6jIyogZDZD"
    }
    headers = {
        "Content-Type" : "application/json"
    }
    data = json.dumps({
        "recipient": {
            "id": recipient_id
        },
        "message": {
            "text" : message_text
        }
    })
    resp = requests.post("https://graph.facebook.com/v2.6/me/messages?access_token=", params=params,headers=headers , data=data)
    print(resp.content)

@app.route('/', methods=['GET'])
def handle_verification():
    if request.args['hub.verify_token'] == VERIFY_TOKEN:
        return request.args['hub.challenge']
    else:
        return "Invalid verification token"

#Handles the message from FB
@app.route('/', methods=['POST'])
def handle_incoming_messages():
    data = request.get_json()

    if data["object"] == "page":
        for entry in data["entry"]:
            for messaging_event in entry["messaging"]:

                if messaging_event.get("message"):
                    sender_id = messaging_event["sender"]["id"]
                    recipient_id = messaging_event["recipient"]["id"]
                    message_text = messaging_event["message"]["text"]

                    reply(sender_id, "yo son")

    return "ok"

if __name__ == '__main__':
    app.run(debug=True)
