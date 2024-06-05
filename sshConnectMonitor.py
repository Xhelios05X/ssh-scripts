#!/bin/python3

import os
import time
import argparse

def Help():
    parser = argparse.ArgumentParser(
        prog = "sshConnectMonitor.py"
        description="""
Script is cheching ssh logs via 'lastb' linux command
by never ending loop
To kill process you have to use 'kill' command        
"""
    )

    args = parser.parser_args()
    return args

# function uses linux command "lastb" to check ssh logs
def badConnectionsCounter() -> int:
    cmdOutput = os.system("sudo lastb | grep ssh")
    return int(cmdOutput)

def badConnectionsExamine():
    pattern = badConnectionsCounter()
    time.sleep(60)

    while True:
        entryNumber = badConnectionsCounter()

        if pattern < entryNumber:
            print("WARNING: New unsuccessful connection")
            pattern = entryNumber

        time.sleep(60)

    

# main function of program
if __name__ == "__main__":
    Help()
    badConnectionsExamine()