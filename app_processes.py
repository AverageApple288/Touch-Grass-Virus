import signal

import psutil
import subprocess
import os
import random

nerdyProcesses = {
    'firefox': 4.75,
    'code': 1,
    'terminal': 1,
    'discord': 99999
}

#Checks if processes with specific name are running
def isRunning(pName):
    try:
        subprocess.check_output(["pgrep", pName])
        return True
    except subprocess.CalledProcessError:
        return False

def getRunningProcessPIDs(pName):
    try:
        pids = []
        pidInBytes = subprocess.check_output(["pgrep", pName])
        for val in pidInBytes.strip().split(b'\n'):
            pids.append(int(val.decode()))
        return pids
    except subprocess.CalledProcessError:
        print(pName, "is not running")
        return []


def getRunningNerdyProcesses():
    allNProcPIDs = []
    #Loop through nerdy processes
    for pName in nerdyProcesses:
        nProcPIDs = getRunningProcessPIDs(pName)
        if len(nProcPIDs) > 0:
            #If there are some running, add it to a list of process PIDs
            allNProcPIDs.append(nProcPIDs)
    return allNProcPIDs


def terminatePIDs(pids):
    for pid in pids:
        os.kill(pid, signal.SIGTERM)

#Terminate named processes with specific name
def terminateProcess(pName):
    for pid in getRunningProcessPIDs(pName):
        os.kill(pid, signal.SIGTERM)
    '''
    try:
        pidInBytes = subprocess.check_output(["pgrep", pName])
        for val in  pidInBytes.strip().split(b'\n'):
            PID = int(val.decode())
            os.kill(PID, signal.SIGTERM)
            print(pName, " with PID ", PID, " has been closed")
    except subprocess.CalledProcessError:
        print(pName, " is not running")
    '''

def terminateRandNerdProcess():
    processes = getRunningNerdyProcesses()
    print(processes)
    randIndex = random.randint(0, len(processes)-1)
    terminatePIDs(processes[randIndex])

terminateRandNerdProcess()






