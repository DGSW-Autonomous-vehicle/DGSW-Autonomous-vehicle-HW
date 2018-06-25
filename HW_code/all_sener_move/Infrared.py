import RPi.GPIO as GPIO
import time
import threading

DR_pin = 16 #pin number
DL_pin = 19

#Infrared Setup

DR = 0
DL = 0

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(DR,GPIO.IN,GPIO.PUD_UP)
GPIO.setup(DL,GPIO.IN,GPIO.PUD_UP)

class Infrared(threading.Thread):
	#flag
	# -1 Error
	# 1 go
	# 2 left
	# 3 rignt

	flag = -1

	def __init__(self):
		threading.Thread.__init__(self)

	def run(self):
		self.read_Inf()

	def read_Inf(self):
			while(1):
				self.DR = GPIO.input(DR_pin)
				self.DL = GPIO.input(DL_pin)

				if(self.DL == 0 and self.DR == 0):
					self.flag = 1

				elif(self.DL == 1 and self.DR == 1):
					self.flag = 0

				elif(self.DL == 0 and self.DR == 1):
					self.flag = 3

				elif(self.DL == 1 and self.DR == 0):
					self.flag = 2
				else:
					self.flag = -1
					print ("DL =")
					print (self.DL)
					print ("DR =")
					print (self.DR)
					print()

				time.sleep(100)
