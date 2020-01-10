import aorusx570_rgb
import time
from random import randint


controller = aorusx570_rgb.AorusRGBController()
while True:
    time.sleep(1)
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    controller.set_rgb("IO_LED",r,g,b)

