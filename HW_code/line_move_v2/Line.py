import RPi.GPIO as GPIO
from AlphaBot2 import AlphaBot2
from TRSensors import TRSensor
import time

TR = TRSensor()
Ab = AlphaBot2()

m = 0
cut = 0

while(1):
    f = 0
    input = TR.AnalogRead()
    for i in range(0,4):
        if(input[i] < 400):
            f += pow(2,i)

    if(f == 0 or f == 31):
	print("zero or full")
	if(m > 0):
	    if(cut == 1):
	        Ab.right()
		time.sleep(0.1)
		cut = 0
  	    elif(cut == 0):
		Ab.left()
	        time.sleep(0.1)
		cut = 1
	    Ab.stop()
	    m -= 1
	Ab.stop()
    elif(f % 4 == 0):
        print("include 4")
        Ab.motor_init()
        Ab.forward()
	m = 7;
    else:
        print("no 4")
        if (f % 16 == 0 or f % 8 == 0):
            print ("left")
            Ab.setMotor_UKC(1,-1)
            Ab.forward()
            m = 7;

        elif (f % 2 == 0 or f % 1 == 0):
            print("right")
            Ab.setMotor_UKC(-1,1)
            Ab.forward()
	    m = 7;

        else:
            print("Error")
            Ab.stop()

        Ab.stop()

    print(bin(f))
    time.sleep(0.1)

