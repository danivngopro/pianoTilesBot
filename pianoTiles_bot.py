import pyautogui as pg
import time
from mss import mss
import keyboard

start_x = 983
start_y = 440

cords_x = [0, 90, 177, 251]

bbox = (start_x,start_y,start_x+252,start_y + 3)

def test_time():
    with mss() as sct:
        t1 = time.time()
        for i in range(100):
            img = sct.grab(bbox)
            pg.click(86,100)
        t2 = time.time()
        print(t2-t1)

def get_mouse_pos():
    while True:
        print(pg.position())
        time.sleep(1)

def get_pixel_color():
    with mss() as sct:
        img = sct.grab(bbox)
        for cord in cords_x:
            print(img.pixel(cord,0))

def start():
    with mss() as sct:
        b = True
        c = cords_x[0]
        while True:
            if keyboard.is_pressed('q'):
                break
            img = sct.grab(bbox)
            if(b == False):
                    if img.pixel(c,2)[0] > 154 and img.pixel(c,2)[0] < 254:
                        pg.mouseUp()
                        b = True
            else:
                for cord in cords_x:
                    if img.pixel(cord,0)[0] < 100:
                        # pg.moveTo(start_x+cord,start_y)
                        pg.mouseDown(start_x+cord,start_y)
                        b = False
                        c = cord
                        # break
                    # while(True):
                    #     print("x,y= " + str(img.pixel(cord,2)) + " pixel: " + str(img.pixel(cord,2)[0]))
                    #     if img.pixel(cord,2)[0] > 154:
                    #         img = sct.grab(bbox)
                    #         pg.mouseUp()
                    #         print("finish click")
                    #         break
                              

time.sleep(1)
start()
#984 474
#1074 479
#1161 474
#1236 488
