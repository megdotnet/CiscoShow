#! python3

import os
import sys
from netmiko import ConnectHandler
from getpass import getpass

ip=sys.argv[1]

def show_cdp_neighbors(lines):
    print("\n")
    
    #for index, item in enumerate(L):
    #next = index + 1
    #if next < len(L):
    #    print index, item, next
    
    ip_found=False
    mgmt_found=False
    
    for item in lines:
        if "Device ID" in item.strip():
            if "SEP6416" in item.strip():
                continue
            else:
                print("       " + item)
        if ip_found:
            if "Platform" in item:
                print("      IP address: [none]")
            else:
                print("      " + item.strip())
            ip_found=False
        if "Entry address" in item.strip(): 
            ip_found=True
        if "Platform" in item: 
            print("        Platform: " + (item.split(" ")[1]) + " " + (item.split(" ")[2]))
        if "Interface" in item: 
            print(" Local Interface: " + ((item.split(" ")[1])[:-1]))
            print("Remote Interface: " + (item.split(" ")[7]))
            print("             --------")
        
    print("\n")
    
def config(ip):
    #cred_user = input("login as: ")
    device = {
    "device_type": "cisco_ios",
    "host": ip,
    "username": "fairbanksm",
    "password": "Sch@ffer42",
    }

    with ConnectHandler(**device) as net_connect:
        lines = net_connect.send_command("show cdp neighbors detail").splitlines() 
        show_cdp_neighbors(lines)
        
config(ip)       
