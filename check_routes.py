'''
sample code for DevNet Express usecase
onbox python code
Author: Alex Feng
email: alfeng@cisco.com

scheduler job name check_rt
python bootflash:/check_routes.py

end-job

scheduler schedule name check_rt_sch
  job name check_rt
  time start 2019:11:29:11:27 repeat 0:0:1

'''
import syslog
import json
import cli


expected_routes = ["1.1.1.1/32","2.2.2.2/32","3.3.3.3/32"]

route_table = cli.clid('sh ip route')
route_table_json = json.loads(route_table)
count = 0

for prefix in route_table_json['TABLE_vrf']['ROW_vrf']['TABLE_addrf']['ROW_addrf']['TABLE_prefix']['ROW_prefix']:
    if prefix['ipprefix'] in expected_routes:
        count +=1

if count == 3:
    syslog.syslog(1,'We got 3 routes , mission completed!!!!!!')
