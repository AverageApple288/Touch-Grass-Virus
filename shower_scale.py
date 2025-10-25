from app_processes import isRunning, nerdyProcesses
import random
import time

#Showerpoints related constants
MAXSP = 600
STARTINGSP = 300
IDLESPDEC = 0.25
SHUTDOWNSP = 0

SPLVLS = [120, 90, 60, 30]
SPPROBS = [30, 20, 15, 7] #n represents probability 1 in n
SPWARNINGS = ["How about you take a break",
"You've been staring at this screen for ages, give your eyes a rest",
"",
""]



NUMEVENTS = 1 #TODO set to final number of events





showerPoints = STARTINGSP
currLvl = 0 #Level n corresponds to values in (n-1)th index of array

#def doEvent(n):

def randomEvent():
    global showerPoints
    if currLvl > 0:
        prob = SPPROBS[currLvl] - 1
        doEvent = random.randint(1, prob)
        if doEvent == 1:
            event = random.randint(1, NUMEVENTS)
def lowerShowerScale():
    global showerPoints
    showerPoints -= IDLESPDEC
    for p, v in nerdyProcesses.items():
        if isRunning(p):
            print(p, v)
            showerPoints -= v


while True:
    lowerShowerScale()
    print(showerPoints)
    time.sleep(1)