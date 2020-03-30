import time 
import random
import pyautogui 
while True:
    if 0 == 0:
        time.sleep(2)
        pyautogui.moveTo(944, 512, duration=3)   
        x = random.randrange(0, 300)
        y = random.randrange(0, 300)
        t = random.randrange(0, 22)
        tt = random.randrange(0, 22)
        slp = random.randrange(0, 15)
        pyautogui.moveRel(x, y, duration=t)
        pyautogui.moveTo(944, 512, duration=tt)
        pyautogui.press('volumedown')
        time.sleep(slp)
        pyautogui.write('The primary keyboard function is write(). \
            This function will type the characters in the string that is passed. \
            To add a delay interval in between pressing each character key, \
            pass an int or float for the interval keyword argument.', interval=0.25)
        pyautogui.press('volumeup')