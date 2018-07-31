# Created by: Farhan Choudhary
# Dated: 10th July, 2018
# LinkedIn: www.linkedin.com/in/farhanchoudhary
# Talk to my Chatbot here: https://cdn.rawgit.com/farhanchoudhary/Chatbot/cc27043b/chatbot.html

# Following Python 3 Installations Required:
# 1. os (environ module)
# 2. sys
# 3. time
# 4. PIL (ImageGrab & Image Modules)
# 5. open cv2 (For Computer Vision)
# 6. numpy
# 7. pyautogui (For GUI Interaction)

import os
import sys
import time
from PIL import ImageGrab
from PIL import Image
from os import environ
import cv2
import numpy as np
import pyautogui as pg
pg.PAUSE = 0


#(x,y) to represent left-top corner of the rectangle for CV object detection - at a distance from the dino
#(x+w,y+h) bottom-right corner of the rectangle enclosing dino and onward collision object

x, y, w, h = 580, 330, 245, 100 #values might change subject to screen resolution

while True:
    img = ImageGrab.grab()
    img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    img = img[ y:y+h, x:x+w ]

    for x0 in range(170,240,5):
        px = img[58,x0]
        if (px[0]<=150):
            print("jump")
            pg.press("up")
            time.sleep(0.05)
            break
