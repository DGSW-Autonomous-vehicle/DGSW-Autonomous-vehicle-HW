import RPi.GPIO as GPIO
import time
import threading

from AlphaBot2 import AlphaBot2
from Infrared import infrared

Ab = AlphaBot2()

In = Infrared()
In.daemon = True
In.start()


try:
    while(1):
        if(In.flag == -1):
            print("Infrared_Error")
        elif(In.flag == 1):
            Ab.forward()
        elif(In.flag == 2):
            Ab.left(30)
        elif(In.flag == 3):
            Ab.right(30)
        else:
            print ("main_Error")


except KeyboardInterrupt:
    GPIO.cleanup()