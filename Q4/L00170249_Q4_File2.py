"""
#
# File       : Q4_L00170249.py
# Created    : 05/11/2021 16:58
# Author     : S.Dunne
#
# Description: Port scanner and show port names when found
#
"""

import socket
import threading

common_ports = {
    "22": "SSH",
    "80": "HTTP"
}

target = "172.16.253.135"  # scan local host
remoteServer = input("Enter a remote host to scan: ")


def port_scanner(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # internet protocol and streaming socket
        s.connect((remoteServer, port))
        if str(port) in common_ports:
            print("{}({}) is OPEN!".format(str(port), common_ports[str(port)]))
        else:
            print("{} is OPEN!".format(port))
    except:
        pass


for port in range(1, 100):  # range of ports to be scanned
    thread = threading.Thread(target=port_scanner, args=[port])
    thread.start()
