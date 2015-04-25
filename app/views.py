from app import app
from flask import render_template, request
from forms import SignUpForm
import requests
import requests.packages.urllib3.contrib.pyopenssl
requests.packages.urllib3.contrib.pyopenssl.inject_into_urllib3()

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
            user_NID = 'N' + data['data']

    return render_template('index.html', first_name=first_name, last_name=last_name, user_NID=user_NID, user_gender=user_gender ,user_email=user_email)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm(request.form)
    if form.validate_on_submit():
        print form.email.data
        print "im inside!"
    return render_template('newUser.html', form=form)

@app.route('/events')
def events():
    headers = {'content-type': 'application/vnd.api+json', 'accept': 'application/vnd.api+json', 'x-api-key': 'uCl5Eg3Morm4alT7Y'}
    r = requests.get('https://api.tnyu.org/v2/events/', headers=headers)
    events = r.json()
    event = events['data']
    title = event[0]['title']
    return title

if __name__ == '__main__':
    app.run()