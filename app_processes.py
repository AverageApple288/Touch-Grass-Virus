import signal

import psutil
import subprocess
import os

nerdyProcesses = {
    'firefox': 1,
    'code': 1,
    'terminal': 1,
    'discord': 100
}

#Checks if processes with specific name are running
def isRunning(pName):
    try:
        subprocess.check_output(["pgrep", pName])
        return True
    except subprocess.CalledProcessError:
        return False

#Terminate named processes with specific name
def terminateProcess(pName):
    try:
        pidInBytes = subprocess.check_output(["pgrep", pName])
        for val in  pidInBytes.strip().split(b'\n'):
            PID = int(val.decode())
            os.kill(PID, signal.SIGTERM)
            print(pName, " with PID ", PID, " has been closed")
    except subprocess.CalledProcessError:
        print(pName, " is not running")






