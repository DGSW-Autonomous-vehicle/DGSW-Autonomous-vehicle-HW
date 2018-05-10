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
	Ab.motor_init()
        Ab.stop()
    elif(f == 4):
	print("forward")
	Ab.motor_init()
	Ab.forward()
    elif(f == 24 or f == 16 or f == 8):
	print("left")
	Ab.setMotor_UKC(2,-3)
	Ab.forward()

    elif(f == 3 or f == 2 or f == 1):
	print("right")
	Ab.setMotor_UKC(-3,2)
	Ab.forward()

    else:
	print("Error")
	Ab.stop()

    print(bin(f))
    time.sleep(0.1)

