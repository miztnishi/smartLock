# Use Raspberry Pi to control Servo Motor motion
# Tutorial URL: http://osoyoo.com/?p=937

import RPi.GPIO as GPIO
import time
import os

GPIO.setwarnings(False)
# Set the layout for the pin declaration
GPIO.setmode(GPIO.BCM)
# The Raspberry Pi pin 11(GPIO 18) connect to servo signal line(yellow wire)
# Pin 11 send PWM signal to control servo motion
GPIO.setup(17, GPIO.OUT)
# Now we will start with a PWM signal at 50Hz at pin 18. 
# 50Hz should work for many servos very will. If not you can play with the frequency if you like.
Servo = GPIO.PWM(17, 50)
# This command sets the left position of the servo
#Servo.start(7.5)
Servo.start(4.5)
# You can play with the values.
# 7.5 is in most cases the middle position
# 12.5 is the value for a 180 degree move to the right
# 2.5 is the value for a -90 degree move to the left
print ("move to the center position:")
#Servo.ChangeDutyCycle(7.5)
time.sleep(1)
print ("move to the right position:")
Servo.ChangeDutyCycle(12.5)
time.sleep(1)
# move to the center position
print ("Move back to the center position.")
#Servo.ChangeDutyCycle(7.5)
#Servo.start(7.5)
#time.sleep(1)
#Servo.stop()

GPIO.setup(18,GPIO.IN,pull_up_down=GPIO.PUD_UP)
sw_status = 1
sw_status = GPIO.input(18)
if sw_status == 0:
    print("Close")
    Servo.ChangeDutyCycle(4.5)
else:
    print("Open!")
time.sleep(1)
Servo.stop()
GPIO.cleanup()
