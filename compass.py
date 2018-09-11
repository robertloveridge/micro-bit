from microbit import *

'''
A simple compass using the micro:bit
'''

compass.calibrate()

while True:
    degrees = compass.heading()
    if degrees < 45:
        display.show("N")
    elif degrees < 135:
        display.show("E")
    elif degrees < 225:
        display.show("S")
    else:
        display.show("W")