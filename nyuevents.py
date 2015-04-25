from flask import Flask
import requests


app = Flask(__name__)


@app.route('/')
def hello_world():
    r = requests.get('https://api.orgsync.com/api/v2/events/83878/timesheets?key=dd6b9d2beb614611c5eb9f56c34b743d1d86f385');
    users = r.json()
    first_name = users[0]['account']['first_name']
    last_name = users[0]['account']['last_name']
    #user_id = users[0]['account']['id']
    user_id = '1918'
    user_link = 'https://api.orgsync.com/api/v2/accounts/%s?key=dd6b9d2beb614611c5eb9f56c34b743d1d86f385' %user_id
    r = requests.get(user_link)
    user =  r.json()
    user_email = user['email']
    user_phone = user['phone_number']
    user_data = user['profile_responses']
    user_gender = None
    user_NID = None
    for data in user_data:
        data_point = data['element']['name']
        if data_point == 'Gender':
            user_gender = data['data']['name']
        elif data_point == 'Student ID':
            user_NID = data['data']



    return 'Hello World!'


if __name__ == '__main__':
    app.run()