# Sending an SMS using the Twilio API
from twilio import rest
# put your own credentials here
account_sid = "ACf8c21d1fd4a593deb2a2d2b45367ec87"
auth_token = "2a7b427096afb43d5d7d6aea03fdcec1"
client = rest.Client(account_sid, auth_token)
message = client.messages.create(
    to="+201286970220",  # vertified phone number from trello
    from_="+14158623509",  # phone number recieved by trello
    body="Tomorrow's forecast in Financial District, San Francisco is Clear",
    media_url="https://climacons.herokuapp.com/clear.png")
print(message.sid)
