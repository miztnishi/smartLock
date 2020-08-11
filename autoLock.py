#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import RPi.GPIO as GPIO
import send_line
import atexit
import pi_servo


def main():
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(18,GPIO.IN,pull_up_down=GPIO.PUD_UP)
  sw_status = 1
  prev_sw_status = 1
  sendline = send_line.SendLine()

  print("start")

  while True:
      try:
        sw_status = GPIO.input(18)
        if prev_sw_status == 0 and sw_status == 1:
           sendline.send("ドアが開きました")
        # 1(open)　0(close)
        ##オートロックは鍵、スマホを忘れて外に出ると締め出されるためなし##
        ##何もなくても開けられる方法を追加する必要あり
        #if prev_sw_status == 1 and sw_status == 0:
          #time.sleep(0.5)
          #piservo = pi_servo.PiServo()
          #piservo.move_close()
          #sendline.send("ドアを閉めました")
        #############################################
        
        time.sleep(0.5)
        prev_sw_status = sw_status

      except Exception as e:
        errMsg = "異常終了です:" + str(e)
        sendline.send(errMsg)
        break

def atExit():
    GPIO.cleanup()

if __name__ == '__main__':
  atexit.register(atExit)
  main()
