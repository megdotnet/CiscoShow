#! python3

import os
import sys
from netmiko import ConnectHandler
from getpass import getpass

ip=sys.argv[1]

def get_kron(lines):
    print("\n")
    for item in lines:
        if ("kron occurrence") in item: 
            print(item)
        if ("policy-list") in item: 
            print(item)
        if ("cli") in item: 
            print(item)
    print("\n")
    
def config(ip):
    cred_user = input("login as: ")
    device = {
    "device_type": "cisco_ios",
    "host": ip,
    "username": cred_user,
    "password": getpass(),
    }

    with ConnectHandler(**device) as net_connect:
        lines = net_connect.send_command("show run").splitlines() 
        get_kron(lines)
        
config(ip)       
