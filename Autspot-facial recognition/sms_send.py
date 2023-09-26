from twilio.rest import Client
account_sid = "ACCOUNT-SID"
auth_token = "AUTH_TOKEN"
client = Client(account_sid, auth_token)
def send_alert(emg_contact):
    message = client.messages.create(body = "Your contact is having an autism  episode", from_ = '+18559254969', to = emg_contact)
    print(message.sid)
