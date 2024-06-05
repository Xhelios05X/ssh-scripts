#!/bin/python3

import os
import time
import argparse

# help function 
def Help():
    parser = argparse.ArgumentParser(
        prog = "sshConnectMonitor.py",
        description="""
Script is cheching ssh logs via 'lastb' linux command
by never ending loop
To kill process you have to use 'kill' command        
        """,
    )

    args = parser.parser_args()
    return args

# function uses linux command "lastb" to check ssh logs
def badConnectionsCounter() -> int:

    # by 'os' library and 'system' method script can run linux commands 
    cmdOutput = os.system("sudo lastb | grep ssh")
    return int(cmdOutput)

# function is checking that ssh logs have a new entry
def badConnectionsExamine():
    pattern = badConnectionsCounter()
    time.sleep(60)

    while True:
        entryNumber = badConnectionsCounter()

        # if ssh logs have a new entry,
        # a warning is printed on the terminal
        # and new the pattern has a new value
        if pattern < entryNumber:
            print("WARNING: New unsuccessful connection")
            pattern = entryNumber

        # after a checking condition, the script sleeps for 1 minute
        time.sleep(60)

# main function of program
if __name__ == "__main__":
    Help()
    badConnectionsExamine()