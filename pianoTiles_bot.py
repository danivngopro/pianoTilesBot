import pyautogui as pg
import time
from mss import mss
import keyboard

start_x = 983
start_y = 474

cords_x = [0, 90, 177, 251]

bbox = (start_x,start_y,start_x+252,start_y + 4)

def get_mouse_pos():
    while True:
        print(pg.position())
        time.sleep(1)

def get_pixel_color():
    with mss() as sct:
        img = sct.grab(bbox)
        for cord in cords_x:
            print(img.pixel(cord,0))
            break

def start():
    with mss() as sct:
        while True:
            if keyboard.is_pressed('q'):
                break
            img = sct.grab(bbox)
            for cord in cords_x:
                if img.pixel(cord,0)[0] < 100:
                    pg.moveTo(start_x+cord,start_y)
                    pg.mouseDown(button='left')
                    if img.pixel(cord,2)[0] > 154:
                        pg.mouseUp(button='left')
                        break

time.sleep(3)
start()
#984 474
#1074 479
#1161 474
#1236 488
