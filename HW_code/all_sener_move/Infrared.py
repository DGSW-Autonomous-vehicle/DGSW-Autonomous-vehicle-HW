import RPi.GPIO as GPIO
import time
import threading

DR_pin = 16 #pin number
DL_pin = 19

#Infrared Setup

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(DR,GPIO.IN,GPIO.PUD_UP)
GPIO.setup(DL,GPIO.IN,GPIO.PUD_UP)

class Infrared(treading.Thread):
	#flag
	# -1 Error
	# 1 go
	# 2 left
	# 3 rignt

	flag = -1

	def run(self):
		self.read_Inf()

	def read_Inf(self):
			while(1):
				self.DR = GPIO.input(DR_pin)
				self.DL = GPIO.input(DL_pin)

				if(self.DL == 1 and self.DR == 1):
					self.flag = 1
				elif(self.DL == 0 and self.DR == 1):
					self.flag = 3
				elif(self.DL == 1 and self.DR == 0):
					self.flag = 2
				else:
					self.flag = -1
				time.sleep(100);
