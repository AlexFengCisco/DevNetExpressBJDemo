'''
   More Fancy

   Smart log server for DevNetExpress use case demo,
   get local host ipv4 address and setup n9kv logging server address
   start log server , wait for misson completed log and count.
   use python nx api and netconf and ansible to config n9kv loopback 1-3 with ipv4 address
   onbox scheduled pythn code check ipv4 routing table , if got expected 3 routes,issue log message mission completed.
   when mission completed log count = 3 ,smart log server clear n9kv loopback 1-3 with nx api.
   mission start over.

   DO NOT FORGET OPEN YOUR LOCAL FIREWALL !!!!

   By Alex Feng
'''
import socket
import requests
import json
import os


# variables credentials
switchuser='admin'
switchpassword='cisco'

# get os ifocnfig ipv4 address , 10. for cisco internal special
if_config = os.popen('''ifconfig | grep "inet 10."''')
inet_v4 = if_config.read().split()
for i in inet_v4:
    if '10.' in i and not '.255' in i: #special for cisco internal
        print(i)
        log_server_ip_address = i


# nx api to config log server with local ipv4  address
config_log_server = 'logging server {ip} port 5000 use-vrf management'.format(ip = log_server_ip_address)
print(config_log_server)
url='http://10.75.58.30/ins'
myheaders={'content-type':'application/json-rpc'}
payload=[
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": config_log_server,
      "version": 1
    },
    "id": 1
  }
]

response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()


# start log server
port = 5000
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("", port))
print("waiting on port: ",port)
count = 0
last_log =''
while 1:
    data, addr = s.recvfrom(1024)
    print(str(data.decode())[7:])

    if 'mission completed!!' in str(data):
        count +=1
        print('mission completed counts ',count)

    if 'mission completed!!' in str(last_log) and 'last message repeated' in str(data):
        count +=1
        print('mission completed counts ',count)

    if count ==2 and 'last message repeated' in str(data) and 'last message repeated' in str(last_log):
        count +=1
        print('mission completed counts ', count)


    if count == 2:
        #clear config interface loopback 1-3
        payload_clear_loopbacks = [
            {
                "jsonrpc": "2.0",
                "method": "cli",
                "params": {
                    "cmd": "no interface loopback1",
                    "version": 1
                },
                "id": 1
            },
            {
                "jsonrpc": "2.0",
                "method": "cli",
                "params": {
                    "cmd": "no interface loopback2",
                    "version": 1
                },
                "id": 2
            },
            {
                "jsonrpc": "2.0",
                "method": "cli",
                "params": {
                    "cmd": "no interface loopback3",
                    "version": 1
                },
                "id": 3
            }
        ]
        response = requests.post(url, data=json.dumps(payload_clear_loopbacks), headers=myheaders,auth=(switchuser, switchpassword)).json()
        print("Interface loopback 1 -3 cleared . mission restarted !!!!")
        count = 0
    last_log = data