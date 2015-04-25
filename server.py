# nothing works since its a WIP but personInAPI() works if you update the name

from flask import Flask
import requests, json
import requests.packages.urllib3.contrib.pyopenssl
requests.packages.urllib3.contrib.pyopenssl.inject_into_urllib3()

app = Flask(__name__)
name = "Abhi Agarwal"

event_id = "541f60e5ff7ba819334c8ffa"

headers = {'content-type': 'application/vnd.api+json', 'accept': 'application/*, text/*', 'x-api-key': 'feWf7yUc5vec3oD7A'}
r = requests.get('https://api.tnyu.org/v2-test/people', headers=headers)
# d = requests.get('https://api.tnyu.org/v2-test/events', headers=headers)
rdata = json.loads(r.text)
#ddata = json.loads(d.text)

# response = requests.put('https://api.tnyu.org/v2-test/event', headers=headers)


@app.route("/")

def personInAPI():
    for i in rdata['data']:
        if name == i['name']:
            # attendee is PERSON in API
            return updateEvent(event_id)
            # return "person in API"

        else:
            return "ERROR: name not in API"

def updateEvent(id):
    d = requests.get('https://api.tnyu.org/v2-test/events/' + id, headers=headers)
    ddata = json.loads(d.text)
#    {"type": "people", "id": "53f54dd98d1e62ff12539db2"}
    a = {"type": "people", "id": "53f54dd98d1e62ff12539db2"}
    unidict = {k.decode('utf8'): v.decode('utf8') for k, v in strdict.items()}


    x = ddata['data']['links']['attendees']['linkage']
    print x
   # for i in x:
    #    print i
        

  
  #  for i in ddata['data']:
   #     for j in i['links']:
    #        print j


if __name__ == "__main__":
    app.run(debug=True)
