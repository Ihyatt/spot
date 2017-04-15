# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient

# Find these values at https://twilio.com/user/account
account_sid = "AC34be416b72bcfa8b49356c52cc173a06"
auth_token = "42f147ed33da65b3a29e9deb79513c33"
client = TwilioRestClient(account_sid, auth_token)


def send_message(body):
	message = client.messages.create(body=body, to="+911", from_="+15623747758")