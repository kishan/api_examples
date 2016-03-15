# need to pip install twilio
import twilio
from twilio.rest import TwilioRestClient 
import os

# import credentials from twilio_variables.py
try:
    from twilio_variables_admin import *
except:
    from twilio_variables import *

def send_sms():
  try:
  	client = TwilioRestClient(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN) 
  	
  	# sends a text
  	message = client.messages.create(
  		to="978-382-3789", 
  		from_="19782917626", 
  		body="another message from TWILIO!!!",  
  	)

  	# sends a text with two images
  	# message = client.messages.create(
  	# 	to="978-382-3789", 
  	# 	from_="19782917626",
  	# 	body="Hello there!",
  	# 	media_url=['https://demo.twilio.com/owl.png', 'https://demo.twilio.com/logo.png'])

  	print message.sid
  	print message.date_created
  	print message.to

  except twilio.TwilioRestException as e:
      print e

def make_call():
  try:
    client = TwilioRestClient(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN) 
    
    call = client.calls.create(
      to="978-382-3789",
      from_="19782917626",
      url="http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient")

    print(call.sid)

  except twilio.TwilioRestException as e:
      print e

# send_sms()
# make_call()

"""
SMS RESPONSE:

{
  "sid": "SMc49fa10c57c14352a81bab518e860cb6",
  "date_created": "Sun, 13 Mar 2016 18:48:39 +0000",
  "date_updated": "Sun, 13 Mar 2016 18:48:39 +0000",
  "date_sent": null,
  "account_sid": "ACb79ada95652fc3c4ee725ee30f20410b",
  "to": "+19783823789",
  "from": "+19782917626",
  "messaging_service_sid": null,
  "body": "Sent from your Twilio trial account - test",
  "status": "queued",
  "num_segments": "1",
  "num_media": "0",
  "direction": "outbound-api",
  "api_version": "2010-04-01",
  "price": null,
  "price_unit": "USD",
  "error_code": null,
  "error_message": null,
  "uri": "/2010-04-01/Accounts/ACb79ada95652fc3c4ee725ee30f20410b/Messages/SMc49fa10c57c14352a81bab518e860cb6.json",
  "subresource_uris": {
    "media": "/2010-04-01/Accounts/ACb79ada95652fc3c4ee725ee30f20410b/Messages/SMc49fa10c57c14352a81bab518e860cb6/Media.json"
  }
}

"""