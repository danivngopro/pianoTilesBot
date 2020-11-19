import pyautogui as pg
import time
from mss import mss
import keyboard
from threading import *

start_x = 983
start_y = 440

cords_x = [0, 90, 177, 251]

bbox = (start_x,start_y,start_x+252,start_y + 3)
                 
class firstRow(Thread):
    def run(self):
        with mss() as sct:
            b = True
            c = cords_x[0]
            while True:
                if keyboard.is_pressed('q'):
                    break
                img = sct.grab(bbox)
                if(b == False):
                        if img.pixel(c,2)[0] > 154 and img.pixel(c,2)[1] > 170 and img.pixel(c,2)[0] < 254:
                            pg.mouseUp()
                            b = True
                else:
                    cord = cords_x[0]
                    if img.pixel(cord,0)[0] < 100:
                        pg.mouseDown(start_x+cord,start_y)
                        b = False
                        c = cord

class secondRow(Thread):
    def run(self):
        with mss() as sct:
            b = True
            c = cords_x[0]
            while True:
                if keyboard.is_pressed('q'):
                    break
                img = sct.grab(bbox)
                if(b == False):
                        if img.pixel(c,2)[0] > 154 and img.pixel(c,2)[1] > 170 and img.pixel(c,2)[0] < 254:
                            pg.mouseUp()
                            b = True
                else:
                    cord = cords_x[1]
                    if img.pixel(cord,0)[0] < 100:
                        pg.mouseDown(start_x+cord,start_y)
                        b = False
                        c = cord

class thirdRow(Thread):
    def run(self):
        with mss() as sct:
            b = True
            c = cords_x[0]
            while True:
                if keyboard.is_pressed('q'):
                    break
                img = sct.grab(bbox)
                if(b == False):
                        if img.pixel(c,2)[0] > 154 and img.pixel(c,2)[1] > 170 and img.pixel(c,2)[0] < 254:
                            pg.mouseUp()
                            b = True
                else:
                    cord = cords_x[2]
                    if img.pixel(cord,0)[0] < 100:
                        pg.mouseDown(start_x+cord,start_y)
                        b = False
                        c = cord

class forthRow(Thread):
    def run(self):
        with mss() as sct:
            b = True
            c = cords_x[0]
            while True:
                if keyboard.is_pressed('q'):
                    break
                img = sct.grab(bbox)
                if(b == False):
                        if img.pixel(c,2)[0] > 154 and img.pixel(c,2)[1] > 170 and img.pixel(c,2)[0] < 254:
                            pg.mouseUp()
                            b = True
                else:
                    cord = cords_x[3]
                    if img.pixel(cord,0)[0] < 100:
                        pg.mouseDown(start_x+cord,start_y)
                        b = False
                        c = cord

time.sleep(1)
r1 = firstRow()
r2 = secondRow()
r3 = thirdRow()
r4 = forthRow()

r1.start()
r2.start()
r3.start()
r4.start()