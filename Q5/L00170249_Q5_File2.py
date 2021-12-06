"""
#
# File       : Q5_L00170249.py
# Created    : 02/12/2021 23:12
# Author     : S.Dunne
#
# Description: Connect to a virtual machine using a python script and install curl. Then create a directory and two
#              sub directories. Then see when the files were last accessed.
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
        connection.send("sudo apt install curl\n")
        time.sleep(1)
        connection.send("shane\n")
        time.sleep(1)
        connection = session.invoke_shell()
        connection.send("mkdir -p labs/{lab1,labs2}\n")  # unix command to list directory contents and save to file
        time.sleep(1)
        connection = session.invoke_shell()
        connection.send("ls -l --time=atime > time\n")
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
