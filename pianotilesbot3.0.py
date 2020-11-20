import pyautogui as pg
import time
from mss import mss
import keyboard
from threading import *

start_x = -1188
start_y = 707

cords_x = [0, 151, 301, 453]
#544
bbox = (start_x,start_y,start_x+454,start_y + 3)

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
            self.chooseClickMethod(c, char)
        
    def chooseClickMethod(self, c, char):
        global currentChar
        with mss() as sct:
            img = sct.grab(bbox)

            # print(str(c) + " - img.pixel(c,113)[0]: " + str(img.pixel(c,113)[0]))
            # print(str(c) + " - img.pixel(c,0)[0]: " + str(img.pixel(c,0)[0]))

            if img.pixel(c,0)[0] > 50 and img.pixel(c,0)[0] < 95 and img.pixel(c,0)[1] > 200 and img.pixel(c,0)[2] > 200 :
                self.mouseClick(img,c)
            elif img.pixel(c,0)[0] < 74:
                self.keyboardClick(img,c,char)

    def mouseClick(self, img, c):
        if img.pixel(c,0)[0] < 74:
            print(str(c) + " - img.pixel(c,93)[0]: " + str(img.pixel(c,0)[0]))
            print(str(c) + " - img.pixel(c,0)[0]: " + str(img.pixel(c,0)[0]))
            pg.mouseUp()
            pg.mouseDown(start_x+c,start_y+1)

    def keyboardClick(self, img, c, char):
        if img.pixel(c,0)[0] < 74:
            currentChar = char
            print(currentChar + " pressed down")
            pg.press(char)

#700 587
#Point(x=-1073, y=308)
time.sleep(2)
r1 = firstRow()
r2 = firstRow()
r3 = firstRow()
r4 = firstRow()

r1.start()
r2.start()
r3.start()
r4.start()


# 444 - img.pixel(c,113)[0]: 105
# 444 - img.pixel(c,0)[0]: 109
# 151 - img.pixel(c,113)[0]: 73
# 151 - img.pixel(c,0)[0]: 110
# 299 - img.pixel(c,113)[0]: 105
# 299 - img.pixel(c,0)[0]: 19
# 0 - img.pixel(c,113)[0]: 106
# 0 - img.pixel(c,0)[0]: 110

# 0 - img.pixel(c,113)[0]: 116
# 0 - img.pixel(c,0)[0]: 120
# 299 - img.pixel(c,113)[0]: 15
# 299 - img.pixel(c,0)[0]: 15  
# 151 - img.pixel(c,113)[0]: 116
# 151 - img.pixel(c,0)[0]: 120
# 444 - img.pixel(c,113)[0]: 113
# 444 - img.pixel(c,0)[0]: 120