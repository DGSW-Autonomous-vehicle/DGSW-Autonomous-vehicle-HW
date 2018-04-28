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

            if ch == ' ':  #공백 즉 스페이스바가 들어 올 경우 정지
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

            elif ch == '8':  #속도 증가
             Ab.speed_up()
             print("speed up now speed : " + Ab.PA)

            elif ch == '2':  # 속도 감소
             Ab.speed_down()
             print("speed down now speed : " + Ab.PA)

            elif ch == '5':  # 속도 초기화
                Ab.setPWMA(50)
                Ab.setPWMB(53)
                print("speed init!")

            elif ch == 'h': #h가 들어오면 프로그램 종효
                Ab.stop()
                run = False
            else :
                Ab.stop()

except KeyboardInterrupt:
        GPIO.cleanup()

