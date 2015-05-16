#README

##OVERVIEW

This script scans the given network for hosts that responds to an ICMP echo.

##USAGE

  -n, --network [NETWORK]    Specifies the network network to be scanned. E.g. 192.168.10.0/24
  -h, --help                 Shows a quick help

##EXAMPLE

Scanning the network 192.168.10.0/24 for alive hosts

  ./lanscan.py -n 192.168.10.0/24

##AUTHOR

This script was written by Christoph Franke (christoph.franke@me.com) in 2015.
