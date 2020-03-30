import pynput
import random
import time
from pynput.mouse import Button, Controller
while True:
    if 0 == 0:
        x = random.randrange(-500, 500)
        y = random.randrange(-500, 500)
        mouse = Controller()
        mouse.position
        mouse.move(x, y)
        time.sleep(1)