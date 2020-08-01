'''The code given below is for text alert when the driver feels drowsy.
sign up on nexmo(now vonage) dashboard and then download private key by creating application'''


import nexmo
from pprint import pprint
#Check for key and secrete id.
client = nexmo.Client(key='1c633cda', secret='0KBrh2luXusABW8P')

client.send_message({
    'from': 'Vonage APIs',
    'to': '917588500675',
    'text': 'Hello from Vonage SMS API',
})



#this code is for text to speech call alert

client = nexmo.Client(
  application_id='400230b2-2e80-4a49-9d43-0ac8597eaa0d',
  private_key='/home/pi/Desktop/private.key',
)
ncco = [
  {
    'action': 'talk',
    'voiceName': 'aditi',
    'text': 'This is a text-to-speech test message.'
  }
]

response = client.create_call({
  'to': [{
    'type': 'phone',
    'number': '917588500675'
  }],
  'from': {
    'type': 'phone',
    'number': '917588500675'
  },
  'ncco': ncco
})

pprint(response)
