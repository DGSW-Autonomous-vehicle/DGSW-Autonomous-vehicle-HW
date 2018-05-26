import RPi.GPIO as GPIO
import time
from AlphaBot2 import AlphaBot2

Ab.AlphaBot2()

DR_pin = 16 #pin number
DL_pin = 19

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(DR,GPIO.IN,GPIO.PUD_UP)
GPIO.setup(DL,GPIO.IN,GPIO.PUD_UP)

try:
	DR = GPIO.input(DR_pin)
	DL = GPIO.input(DL_pin)
	#print(DR,DL)
	if(DL == 1 and DR == 1):
		Ab.forward()
		#print("forward")
	elif(DL == 0 and DR == 1):
		Ab.right(20)
		time.sleep(0.3)
	elif(DL == 1 and DR == 0):
		Ab.left(20)
		time.sleep(0.3)
	else:
		Ab.stop()

except KeyboardInterruqt:
	GPIO.cleanup()
