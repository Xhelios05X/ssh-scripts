#!/bin/python3

import paramiko
import argparse
import sys

def Help():
    parser = argparse.ArgumentParser(
        prog = "sshConnect.py",
        description = """
Scrpit connect to host via ssh connection and execute 
commands
        """,
    )

    parser.add_argument("-o", "--other", action="store_true")
    parser.add_argument("hostIP")
    parser.add_argument("username")
    parser.add_argument("password")

    args=parser.parse_args()
    return args

def Commands(commands:list, other=False):
    if other:
        pass

def SSHconnect(hostIP:str, username:str, password:str, execCommands:list):
    client = paramiko.client.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostIP, port=22, username=username, password=password)
    _stdin, _stdout, _stderr = client.exec_command("ls")
    print(_stdout.read().decode())
    client.close()

# main function of script
if __name__ == "__main__":
    help = Help()

    if help.other:
        execCommands = sys.argv[4:]
    else:
        execCommands = ("ls", "ps",)
    hostIP = sys.argv[1]
    username = sys.argv[2]
    password = sys.argv[3]
    
    SSHconnect(hostIP, username, password, execCommands)