import signal
from tokenize import String

import psutil
import subprocess
import os

process_name = "firefox"

try:

    PID = int(subprocess.check_output(["pgrep", process_name]).strip().decode())
    print(PID)

    os.kill(PID, signal.SIGTERM)
    #print(process_name, " with PID ", PID, " has been closed")

except subprocess.CalledProcessError:
    print(process_name, " is not running")
'''

for process in psutil.process_iter():
    print(process.cmdline())

'''