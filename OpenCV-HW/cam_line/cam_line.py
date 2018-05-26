import RPi.GPIO as GPIO
import time
import threading

from AlphaBot2 import AlphaBot2
from Camera_Line import Camera_Line

Ab = AlphaBot2()
CL = Camera_Line()

t_CL = threading.Thread(target=CL.main())
t_CL.start()

while(ture):

    flag_CL = CL.flag

    if(flag_CL == -1):
        Ab.stop()
        print("no input data")

    elif(flag_CL == 0):
        Ab.motor_init()
        Ab.forward()
        print("forward")

    elif(flag_CL == 1):
        print("right")
        Ab.setMotor_UKC(-1, 1)
        Ab.forward()

    elif (flag_CL == 2):
        print ("left")
        Ab.setMotor_UKC(1, -1)
        Ab.forward()

    else:
        Ab.motor_init()
        Ab.stop()
        print("Error")

    time.sleep(0.05)
