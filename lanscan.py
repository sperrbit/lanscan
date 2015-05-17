#!/usr/bin/python

import os
from netaddr import *
import argparse
import subprocess
import socket

# DNS Lookup
def lookup(addr):
    try:
        return socket.gethostbyaddr(str(addr))
    except:
        return None, None, None

# Pasring the Arguments
parser = argparse.ArgumentParser(description='LAN-SCAN')
parser.add_argument('-n','--network', help='e.g. 192.168.10.0/24', required=True)
parser.add_argument('-d','--dns', help='Set DNS lookup True or False')

args = vars(parser.parse_args())
network = str(args['network'])
dns = str(args['dns'])

# Check if DNS Lookup-Argument is set
if(dns==None):
    nslookup=True
elif(dns=="True"):
    nslookup=True
elif(dns=="False"):
    nslookup=False
else:
    nslookup=True

# Check-Loop
print ("\nScanning "+network+" for hosts...\n")

print ("IP\t\tStatus\tName")
print ("--\t\t------\t-----")
count = 0
hostssalive =""
ips = 0
for ip in IPSet([network]):
    try:
        response = subprocess.check_output(
        ["ping", "-c", "1", "-n", "-W", "1", "-i","0.1", str(ip)],
        stderr=subprocess.STDOUT,
        universal_newlines=True)

        if (nslookup):
            name,alias,addresslist = lookup(ip)
            if (name==None):
                name = ""
        else:
            name = ""
        print (str(ip)+"\tALIVE\t"+name)

        count += 1
        if (name != ""):
            hostssalive += str(ip)+"\t"+name+"\n"
        else:
            hostssalive += str(ip)+"\n"

    except subprocess.CalledProcessError:
        response = None

        print (str(ip))
    ips = ips +1

# Summary
print ("\nSummary:\n--------\n"+str(ips)+" hosts scanned.")

if (int(count) == 1):
    print (str(count)+" host alive")
else:
    print (str(count)+" hosts alive")

if (hostssalive != ""):
    print ("\n"+hostssalive)
else:
    print ("")
