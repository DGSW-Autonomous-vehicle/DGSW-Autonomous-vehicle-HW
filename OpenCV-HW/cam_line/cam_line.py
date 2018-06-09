import RPi.GPIO as GPIO
import time
import threading

from AlphaBot2 import AlphaBot2
from Camera_Line import Camera_Line

Ab = AlphaBot2()

CL = Camera_Line()
CL.daemon = True
CL.start()

try:
    while(1):

        flag_CL = CL.flag

        if(flag_CL == -1):
            Ab.stop()
            print("no input data")

        elif(flag_CL == 0):
            Ab.motor_init()
            Ab.forward()
            print("forward")

        elif(flag_CL == 2):
            print("right")
            Ab.setMotor_UKC(-1, 0)
            Ab.forward()

        elif (flag_CL == 1):
            print ("left")
            Ab.setMotor_UKC(0, -1)
            Ab.forward()

        else:
            Ab.motor_init()
            Ab.stop()
            print("Error")

        time.sleep(0.05)

except KeyboardInterrupt:
    GPIO.cleanup()