# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient

# Find these values at https://twilio.com/user/account
account_sid = "ACXXXXXXXXXXXXXXXXX"
auth_token = "YYYYYYYYYYYYYYYYYY"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(to="+14085610268", from_="+15623747758",
                                     body="Hello there!",
                                     media_url=['https://demo.twilio.com/owl.png', 'https://demo.twilio.com/logo.png'])