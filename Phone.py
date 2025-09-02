from twilio.rest import Client
import os

account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
twilio_phone_number = "your_twilio_phone_number"

def make_phone_call(to_number):
    """
    Makes an outbound phone call and plays a message using the Twilio API.
    """
    try:
        client = Client(account_sid, auth_token)
        call = client.calls.create(
            twiml='<Response><Say>Hello, this is an automated call from your Python script.</Say></Response>',
            to=to_number,
            from_=twilio_phone_number
        )
        print(f"Call initiated successfully! SID: {call.sid}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    recipient = "+919876543210"
    make_phone_call(recipient)
