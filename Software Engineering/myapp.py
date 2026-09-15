import requests
import json

URL = "http://127.0.0.1:8000/creatstudent/"

data = {
    'name': 'Nasimul Islam',
    'roll':45,
    'section':'6DM'
}
json_data = json.dumps(data)

r = requests.post(url= URL, data = json_data)
res_data = r.json()

data = {
    'id':5,
    'name':'Araf',
    'roll':43,
    'section':'7DM'
}
json_data = json.dumps(data)
r = requests.put(url=URL,data = json_data)
res = r.json()
print(res)

data = {
    'id':4,
    'name':'Debojit Barua'
}
json_data = json.dumps(data)
r = requests.patch(url=URL,data = json_data)
res = r.json()
print(res)


data = {
    'id':9,
}
json_data = json.dumps(data)
r = requests.delete(url=URL,data = json_data)
res = r.json()
print(res)    