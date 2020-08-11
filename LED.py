import RPi.GPIO as GPIO
import time

#確認
#set BCM_GPIO 18(GPIO1) as LED pin
LEDPIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(LEDPIN,GPIO.OUT)
for x in range(5):
    GPIO.output(LEDPIN,True)
    time.sleep(2)
    GPIO.output(LEDPIN,False)
    time.sleep(2)
GPIO.cleanup()

    
