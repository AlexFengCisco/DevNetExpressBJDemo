##  Use case  demo for DevNetExpress BJ

### Homework , NX OS programming config and automatic check , offbox & onbox.

#### Prepare Lab enviroment
    
    N9Kv version: 9.2.3 or higher
    python 3.7.5
    ansible 2.6.2
    pre config n9kv to support NX-API Netconf SSH
    notice : feature lldp is needed to avoid ansible gather facts error
    
    python modules, check requirements.txt
    ansible==2.6.2
    asn1crypto==0.24.0
    bcrypt==3.1.4
    certifi==2018.4.16
    cffi==1.11.5
    chardet==3.0.4
    cryptography==2.5
    future==0.18.2
    idna==2.7
    Jinja2==2.10
    lxml==4.2.4
    MarkupSafe==1.0
    ncclient==0.6.0
    paramiko==2.6.0
    pyang==1.7.5
    pyasn1==0.4.4
    pycparser==2.18
    PyNaCl==1.2.1
    PyYAML==5.1.2
    requests==2.22.0
    six==1.11.0
    textfsm==1.1.0
    urllib3==1.23
    xmltodict==0.11.0
    
#### Task 1

    Config N9kv interface Loopback 1 and ipv4 address 1.1.1.1/32 via python NX API code
    
#### Task 2

    Config N9kv interface Loopback 2 and ipv4 address 2.2.2.2/32 via python Netconf code
    
#### Task 3 

    Config N9kv interface Loopback 3 and ipv4 address 3.3.3.3/32 via ansible playbook
    
#### Task 4

    NX OS scheduled onbox python code checks N9kv routing table each 60 seconds,
    if all "1.1.1.1/32 2.2.2.2/32 3.3.3.3/32" in routing table , 
    issue log message "We got 3 routes , mission completed!!!"
    
    in N9kv console, show logging to check the log issued by python.
    
#### Task 5

    When task 1-4 finished ,Submit your code to your gihub, and send github link to instructor
    
#### Useful Links

    https://docs.ansible.com/ansible/latest/modules/list_of_network_modules.html
    
    https://github.com/CiscoDevNet/devnet-express-dci-code-samples
    
    https://github.com/ncclient/ncclient/tree/master/examples
    
    https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus9000/sw/92x/programmability/guide/b-cisco-nexus-9000-series-nx-os-programmability-guide-92x.html
    
#### More fancy 

    A python Smart log server , 
    when 'mission  completed!!' log received , trigger NX API to clear interface Loopback 1-3,
    mission start over.