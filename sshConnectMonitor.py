#!/bin/python3

import os

# function uses unixlike command "lastb" to check 
def badConnectionsCounter() -> int:
    cmdOutput = os.system("sudo lastb | grep ssh")
    return int(cmdOutput)

def badConnectionsExamine():
    pass

# main function of program
if __name__ == "__main__":
    badConnectionsExamine()