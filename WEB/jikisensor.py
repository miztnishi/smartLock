#確認用

import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

 
GPIO.setup(18,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.OUT)
Servo = GPIO.PWM(17, 50)
sw_status = 1
Servo.start(12.5)

while True:
    try:
        sw_status = GPIO.input(18)
        if sw_status == 0:
            print("Close")
            Servo.ChangeDutyCycle(4.5)
        else:
            print("Open!")
            Servo.ChangeDutyCycle(7.5)

        time.sleep(0.1)
    except:
        break

GPIO.cleanup()
print("end")
