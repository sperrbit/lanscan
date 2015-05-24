#LANSCAN

##Overview

This script scans the given network for hosts that responds to an ICMP echo.

##Usage

    -n, --network [NETWORK]
    Specifies the network network to be scanned. E.g. 192.168.10.0/24.

    -d, --dns [TRUE or FALSE]
    Enables oder disables the name-server-lookup. The default-value is True.

    -l, --logging [TRUE or FALSE]
    Enables or disables logging. Default is False. Logging will create a CSV-File in the script dir.

    -h, --help
    Shows a quick help-message

##Example

Scanning the network 10.20.0.0/30 for alive hosts:

    $ ./lanscan.py -n 10.20.0.0/30

Example output:

    Scanning 10.20.0.0/30 for hosts...

    IP          Status  Name
    --		    ------  ----
    10.20.0.0
    10.20.0.1   ALIVE   rtr001
    10.20.0.2   ALIVE   rtr002
    10.20.0.3

    Summary:
    --------
    4 hosts scanned
    2 hosts alive

    10.20.0.1 (rtr001)
    10.20.0.2 (rtr002)

##Contact

You can contact me via mail: [mail@sysadmin-log.de](mail@sysadmin-log.de).
