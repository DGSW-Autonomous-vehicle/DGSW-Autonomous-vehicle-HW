import RPi.GPIO as GPIO
import time
from AlphaBot2 import AlphaBot2

Ab = AlphaBot2()

DR = 16
DL = 19

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(DR,GPIO.IN,GPIO.PUD_UP)
GPIO.setup(DL,GPIO.IN,GPIO.PUD_UP)

try:
	while True:
		DR_status = GPIO.input(DR)
		DL_status = GPIO.input(DL)
		print(DR_status,DL_status)
		if((DL_status == 0) or (DR_status == 0)):
			Ab.back()
			time.sleep(0.3)

			Ab.left(20)
			#Ab.right(20)
			time.sleep(0.2)
			Ab.stop()
		#	print("object")
		else:
			Ab.forward()
		#	print("forward")

except KeyboardInterrupt:
	GPIO.cleanup();

