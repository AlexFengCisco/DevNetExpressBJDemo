import requests
import json


my_headers = {'content-type': 'application/json-rpc'}
url = "http://10.75.58.30/ins"
username = "admin"
password = "cisco"


myheaders={'content-type':'application/json-rpc'}
payload=[
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "int loop 1",
      "version": 1
    },
    "id": 1
  },
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "ip address 1.1.1.1/32",
      "version": 1
    },
    "id": 2
  },
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "no shu",
      "version": 1
    },
    "id": 3
  }
]
response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(username,password)).json()
print(response)