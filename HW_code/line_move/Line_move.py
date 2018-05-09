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
        if(input[i] < 400):
            f += pow(2,i)

    if(f == 0 or f == 31):
        print("zero or full")
        Ab.stop()

    elif(8 > f):
        if(f % 1 == 0 and f % 2 == 0):
            print("8 > forword")
            Ab.motor_init()
            Ab.forward()
        else:
            print("right")
            Ab.setMotor_UKC(-5, 5)
            Ab.forward()
    elif(f < 3):
        print("left")
        Ab.setMotor_UKC(5,-5)
        Ab.forward()

    elif(f == 4):
        print("forword")
        Ab.motor_init()
        Ab.forward()
    else:
        print("else")
        Ab.stop()

    print(bin(f))
    time.sleep(0.1)
