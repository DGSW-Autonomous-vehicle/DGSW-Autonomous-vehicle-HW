import RPi.GPIO as GPIO
from AlphaBot2 import AlphaBot2
from TRSensors import TRSensor
import time

TR = TRSensor()
Ab = AlphaBot2()

while(1):
    f = 0
    input = TR.AnalogRead()
    for i in range(0,4):
        if(input[i] < 300):
            f += 2^i
    print (bin(f))
    time.sleep(1)