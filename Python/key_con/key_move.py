import RPi.GPIO as GPIO
import time
from AlphaBot2 import AlphaBot2
import sys, tty, termios

Ab = AlphaBot2()

run = True

print("'h' key is exit")

try:

        while run:
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            tty.setraw(sys.stdin.fileno())

            ch = sys.stdin.read(1)
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

            if ch == ' ':  
                 Ab.stop()
                 print("stop")

            elif ch == 'w':
                 Ab.forward()
                 print("up")

            elif ch == 'd':
                 Ab.right()
                 print("right")

            elif ch == 'a':
                Ab.left()
                print("left")

            elif ch == 's':
                Ab.backward()

            elif ch == '8':
                if(Ab.PA <= 90):
                    Ab.speed_up()
                    print("speed up now speed :" ,Ab.PA)
                else:
                    print("speed max");

            elif ch == '2':
                if (Ab.PA >= 30):
                    Ab.speed_down()
                    print("speed down now speed :", Ab.PA)
                else:
                    print("speed min");

            elif ch == '5':
                Ab.setPWMA(50)
                Ab.setPWMB(50)
                print("speed init!")

            elif ch == 'h':
                Ab.stop()
                run = False
            else :
                Ab.stop()

except KeyboardInterrupt:
        GPIO.cleanup()

