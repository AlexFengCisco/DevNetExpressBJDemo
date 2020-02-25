import requests
import json


'''
   change copy artifact server ip address first!!!!!
   then start http service !!!
   
'''


switchuser='admin'
switchpassword='cisco'

url='http://10.75.58.30/ins'
myheaders={'content-type':'application/json-rpc'}
payload=[
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "copy http://10.79.101.3:8000/check_routes.py bootflash:///check_routes.py vrf management",
      "version": 1
    },
    "id": 1
  }
]
response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()
#print(response)
copy_result = response['result']['msg']

if 'Copy complete.' in copy_result:
    #print("Upload file to NX OS Complete.")
    print "Upload file to NX OS Complete."
else:
    #print("Upload failed.")
    print "Upload failed."
