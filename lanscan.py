#!/usr/bin/python

import os
from netaddr import *
import argparse
import subprocess
import socket

parser = argparse.ArgumentParser(description='LAN-SCAN')
parser.add_argument('-n','--network', help='e.g. 192.168.10.0/24', required=True)

args = vars(parser.parse_args())

network = str(args['network'])

print ("\nScanning "+network+" for hosts...\n")
count = 0
hostssalive =""
for ip in IPSet([network]):
    try:
        response = subprocess.check_output(
        ["ping", "-c", "1", "-n", "-W", "1", "-i","0.1", str(ip)],
        stderr=subprocess.STDOUT,
        universal_newlines=True)
        print (str(ip)+"\tis alive")

        count += 1
        hostssalive += str(ip)+"\n"

    except subprocess.CalledProcessError:
        response = None

        print (str(ip))

if (int(count) == 1):
    print ("\nSummary\n--------\n"+str(count)+" host alive")
else:
    print ("\nSummary:\n--------\n"+str(count)+" hosts alive")

print ("\n"+hostssalive)
