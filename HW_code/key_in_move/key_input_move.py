import RPi.GPIO as GPIO
import time
from AlphaBot2 import AlphaBot2

Ab = AlphaBot2()

try:
	while True:
        s = input();

		if s = ' ':
			Ab.stop();
			print("stop")
		elif s = 'w':
			Ab.forward();
			print("up")
		elif s = 'd':
			Ab.right();
			print("right")
			while GPIO.input(B) == 0:
				time.sleep(0.01)
		elif s = 'a':
			Ab.left();
			print("left")

		elif s = 's':
			Ab.backward();
			print("down")
		else:


except KeyboardInterrupt:
	GPIO.cleanup()