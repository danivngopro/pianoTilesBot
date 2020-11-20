import pyautogui as pg
import time
from mss import mss
import keyboard
from threading import *

start_x = -1186
start_y = 707

cords_x = [0, 151, 299, 444]

bbox = (start_x,start_y,start_x+445,start_y + 1)

counter = 0

currentChar = ''

class firstRow(Thread):

    def run(self):
        global counter
        c = cords_x[counter]
        if counter == 0:
            char = 'a'
        elif counter == 1:
            char = 's'
        elif counter == 2:
            char = 'd'
        elif counter == 3:
            char = 'f'
        counter += 1
        while True:
            if keyboard.is_pressed('q'):
                break
            self.clickAndRelease(c, char)
        
    def clickAndRelease(self, c, char):
        global currentChar
        with mss() as sct:
            img = sct.grab(bbox)
            if img.pixel(c,0)[0] < 74:
                if(currentChar != char):
                    currentChar = char
                    pg.press(char)



time.sleep(2)
r1 = firstRow()
r2 = firstRow()
r3 = firstRow()
r4 = firstRow()

r1.start()
r2.start()
r3.start()
r4.start()
