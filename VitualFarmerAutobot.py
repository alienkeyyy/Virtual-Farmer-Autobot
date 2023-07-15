import random
import requests
import time
import hashlib
import string

# ==============| EDIT THIS |==============
userToken='USERTOKEN'
botToken='BOT_TOKEN'
message_url='MESSAGE_URL'
user_id='USER_ID'
# ==============| EDIT THIS |==============

guild_id, channel_id, message_id = message_url.split('/')[-3:]
random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=32))
session_id = hashlib.md5(random_string.encode()).hexdigest()

def gather():
    global userToken, channel_id, message_id, guild_id
    nonce=''.join(random.choice('0123456789') for _ in range(19))
    url = 'https://discord.com/api/v9/interactions'
    headers = {
        'authorization': userToken,
        'content-type': 'application/json'}
    data = {
        'type': 3,
        'nonce': nonce,
        'guild_id': guild_id,
        'channel_id': channel_id,
        'message_flags': 0,
        'message_id': message_id,
        'application_id': '631216892606152714',
        'session_id': session_id,
        'data': {
            'component_type': 2,
            'custom_id': 'gather '+user_id
        }
    }

    response = requests.post(url, headers=headers, json=data)
    print('Gather sent. Response code:', response.status_code)   

def sell():
    global userToken, channel_id, message_id, guild_id
    nonce=''.join(random.choice('0123456789') for _ in range(19))
    url = 'https://discord.com/api/v9/interactions'
    headers = {
        'authorization': userToken
        }
    data = {
        'type': 3,
        'nonce': nonce,
        'guild_id': guild_id,
        'channel_id': channel_id,
        'message_flags': 0,
        'message_id': message_id,
        'application_id': '631216892606152714',
        'session_id': session_id,
        'data': {
            "component_type": 2,
            "custom_id": "sell"
        }
    }

    response = requests.post(url, headers=headers, json=data)
    print('Sell sent. Response code:', response.status_code)

def readMsg():
    global botToken, channel_id, message_id, guild_id
    
    api_url = f'https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}'
    headers = {'Authorization': 'Bot ' + botToken}
    response = requests.get(api_url, headers=headers)
    data = response.json()

    description = data['embeds'][0]['description']
    start_index = description.find('**') + 2
    end_index = description.find('**', start_index)
    dynamic_string = description[start_index:end_index]

    return dynamic_string

def verify(verifyCode):
    global userToken, channel_id, message_id, guild_id
    nonce = ''.join(random.choice('0123456789') for _ in range(19))

    url = 'https://discord.com/api/v9/interactions'
    headers = {
        'Authorization': userToken,
    }

    payload = {
        'type': 2,
        'application_id': '631216892606152714',
        'guild_id': guild_id,
        'channel_id': channel_id,
        'session_id': session_id,
        'data': {
            'version': '937527220426145829',
            'id': '935381357692092517',
            'name': 'verify',
            'type': 1,
            'options': [
                {
                    'type': 3,
                    'name': 'answer',
                    'value': verifyCode
                }
            ]
        },
        'nonce': nonce
    }

    response = requests.post(url, headers=headers, json=payload)
    print(response.text)

while True:
    if len(readMsg())==6 and readMsg()[0]!='$':
        verify(readMsg())
    for i in range(5):
        time.sleep(2.3)
        gather()
    sell()
