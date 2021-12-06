"""
#
# File       : L00170249_Q3.py
# Created    : 04/11/2021 16:19
# Author     : S.Dunne
#
# Description: Connect to the virtual machine using a python script using the ssh port. Establish that the connection
#  was successful
#
"""

import paramiko
import time
import re


# Open SSH connection to the device
def ssh_connection(ip):
    try:
        username = "shane"
        password = "shane"
        print("Establishing a connection...")
        session = paramiko.SSHClient()
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        session.connect(ip.rstrip("\n"), username=username, password=password)
        connection = session.invoke_shell()
        connection.send("ls -al > ShaneDunne.txt\n")  # unix command to list directory contents and save to file
        time.sleep(1)

        vm_output = connection.recv(65535)
        if re.search(b"% Invalid input", vm_output):
            print("There was an error on vm {}".format(ip))
        else:
            print("Commands successfully executed on {}".format(ip))
        session.close()
    except paramiko.AuthenticationException:
        print("Authentication Error")


ssh_connection("172.16.253.135")  # ip address of VM
