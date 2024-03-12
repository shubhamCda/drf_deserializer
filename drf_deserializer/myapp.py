import json
import requests

URL=""

data = {
    'name':'Shubham',
    'roll':'101',
    'city':'Nagpur'
}

json_data = json.dumps(data)

r = requests.post(URL, data=json_data)

data = r.json()
print(data)