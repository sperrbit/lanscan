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

    -o, --online [TRUE or FALSE]
    True shows only online hosts. Default is true

    -h, --help
    Shows a quick help-message

##Example

Scanning the network 192.168.178.0/30 for alive hosts:

    $ ./lanscan.py -n 192.168.178.0/30

Example output:

    ** Scanning 192.168.178.0/30 for hosts **

    100%|#############################################|Time: 0:00:01


    +---------------+--------+-----------+
    | IP Address    | Status | Name      |
    +---------------+--------+-----------+
    | 192.168.178.1 | ONLINE | rtr001    |
    | 192.168.178.2 | ONLINE | rtr002    |
    +---------------+--------+-----------+


    +-------------+-----------+
    | IPs scanned | IPs alive |
    +-------------+-----------+
    | 4           | 2         |
    +-------------+-----------+

##Contact

You can contact me via mail: [mail@sysadmin-log.de](mail@sysadmin-log.de).
