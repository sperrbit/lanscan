#!/usr/bin/python

import os
from netaddr import *
import argparse
import subprocess

parser = argparse.ArgumentParser(description='LAN-SCAN')
parser.add_argument('-t','--target', help='e.g. 192.168.10.0/24', required=True)
args = vars(parser.parse_args())

target = str(args['target'])

#print ("Scanning "+target+" for hosts...)

for ip in IPSet([target]):
    try:
        response = subprocess.check_output(
        ["ping", "-c", "1", "-n", "-W", "1",  str(ip)],
        stderr=subprocess.STDOUT,  # get all output
        universal_newlines=True  # return string not bytes
    )
        print (str(ip)+"\tis alive")

    except subprocess.CalledProcessError:
        response = None

        print (str(ip))
