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

    if(f == 8):
	print("forward")
	Ab.setMotor_UKC(-3,2)
	Ab.forward()
    elif(f == 2):
	print("left")
	Ab.setMotor_UKC(2,-3)
	Ab.forward()
    else:
	print("forward")
	Ab.motor_init()
	Ab.forward()

    print(bin(f))
    time.sleep(0.1)

