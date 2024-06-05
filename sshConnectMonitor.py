#!/bin/python3

import os
import time

# function uses unixlike command "lastb" to check 
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
    badConnectionsExamine()