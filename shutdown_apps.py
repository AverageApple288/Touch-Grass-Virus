import signal
from tokenize import String

import psutil
import subprocess
import os




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


terminateProcess("code")
terminateProcess("terminal")
terminateProcess("firefox")

