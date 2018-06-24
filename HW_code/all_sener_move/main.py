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


except KeyboardInterrupt:
    GPIO.cleanup()