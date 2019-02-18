#!/usr/bin/python

# Christoph Franke
# mail@cfranke.org
# 12.02.2019

from netaddr import *
import socket
import subprocess
import argparse
import signal
import sys

# Catch SIGIN STRG+C
def signal_handler(sig, frame):
        print('Scan stopped.')
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

# Portscan
def checkPort(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.3)
        result = s.connect((ip, port))
        s.shutdown(1)
        return True
    except:
        return False

# Reverse Lookup
def lookup(addr):
    try:
        data = socket.gethostbyaddr(str(addr))
        host = repr(data[0])
        host = str(host)
        host = host.strip("'")
        return host
    except:
        return "NA"

# Color Output
col_green =  "\033[0;32m"
col_red = "\033[1;31m"
col_norm = "\033[0m"

# Pasring the Arguments
parser = argparse.ArgumentParser(description='Subnet Scanner')
parser.add_argument('-n','--network', help='e.g. 192.168.10.0/24', required=True)
parser.add_argument('-t','--timeout', help='timeout in seconds', default='0.2')
args = vars(parser.parse_args())
network = str(args['network'])
timeout = str(args['timeout'])

ftp = "0"
ssh = "0"
http = "0"
https = "0"
smb = "0"
rdp = "0"

# Print Header
print ("IP, STATUS, HOSTNAME, ftp, ssh, http, https, smb, rdp")

# Loop through Subnet and try to ping and portscan host
for ip in IPSet([network]):
    try:
        response = subprocess.check_output(
        ['ping', '-c', '3', "-W", "1", "-i",timeout, str(ip)],
        stderr=subprocess.STDOUT,
        universal_newlines=True)
        online = True
        icmp = True
        hostname = str(lookup (str(ip)))
        if (checkPort(str(ip), 21)):
            online = True
            ftp = "1"
        if (checkPort(str(ip), 22)):
            online = True
            ssh = "1"
        if (checkPort(str(ip), 80)):
            online = True
            http = "1"
        if (checkPort(str(ip), 443)):
            online = True
            https = "1"
        if (checkPort(str(ip), 445)):
            online = True
            smb = "1"
        if (checkPort(str(ip), 3389)):
            online = True
            rdp = "1"
        if (online == True):
            print (str(ip)+ ", " +col_green +"ONLINE"+col_norm+", "+hostname+", "+ftp+", "+ssh+", "+http+", "+https+", "+smb+", "+rdp)
        else:
            print (str(ip)+", "+col_red+"OFFLINE"+col_norm+", NA")

        ftp = "0"
        ssh = "0"
        http = "0"
        https = "0"
        smb = "0"
        rdp = "0"

# Catch Error
    except subprocess.CalledProcessError:
        print (str(ip)+", "+col_red+"OFFLINE"+col_norm+", NA")
