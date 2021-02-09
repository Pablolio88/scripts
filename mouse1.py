import time 
import random
import pyautogui 
while True:
    if 0 == 0:
        time.sleep(20)
        pyautogui.moveTo(944, 512, duration=3)   
        x = random.randrange(0, 300)
        y = random.randrange(0, 300)
        t = random.randrange(0, 22)
        tt = random.randrange(0, 22)
        slp = random.randrange(0, 15)
        interv = 0.25
        pyautogui.moveRel(x, y, duration=t)
        pyautogui.moveTo(944, 512, duration=tt)
        pyautogui.press('volumedown')
        time.sleep(slp)
        pyautogui.write('A VPC peering connection is a networking connection between two VPCs that enables you to route traffic between them privately.\
             Instances in either VPC can communicate with each other as if they are within the same network.\
                  You can create a VPC peering connection between your own VPCs, with a VPC in another AWS account, or with a VPC in a different AWS Region.', interval=interv)
        pyautogui.press('volumeup')