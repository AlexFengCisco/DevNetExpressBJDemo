import os
if_config = os.popen('''ifconfig | grep "inet 10."''')
inet_v4 = if_config.read().split()
for i in inet_v4:
    if '10.' in i: #special for cisco internal
        ipv4_add = i

