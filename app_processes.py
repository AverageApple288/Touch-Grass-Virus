import signal

import psutil
import subprocess
import os
import random

from close_firefox_window import close_firefox_run
from close_terminal_window import close_terminal_run
from close_code_editor_window import close_code_editor_run



nerdyProcessPoints = {
    'firefox': 4.75,
    'code': 1,
    'terminal': 1,
    'discord': 99999
}

nerdyProcessMessages = {
    'firefox': close_firefox_run,
    'code': close_code_editor_run,
    'terminal': close_terminal_run,
    'discord': lambda : print("Discord Mod")
}

#Checks if processes with specific name are running
def isRunning(pName):
    try:
        subprocess.check_output(["pgrep", pName])
        return True
    except subprocess.CalledProcessError:
        return False

#Returns th
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
    NerdProgs = []
    #Loop through nerdy processes
    for pName in nerdyProcessPoints:
        NerdProccesses = getRunningProcessPIDs(pName)
        if len(NerdProccesses) > 0:
            #If there are some running, add it to a list of process PIDs
            NerdProgs.append((pName, NerdProccesses))
    return NerdProgs


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
    terminatePIDs(processes[randIndex][1])
    print(processes[randIndex][0], "was terminated")

terminateRandNerdProcess()






