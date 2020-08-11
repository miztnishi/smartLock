#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

class PiServo:
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(17, GPIO.OUT)

#右回り　閉める
  def move_close(self):
    Servo = GPIO.PWM(17, 50)
    Servo.start(1.5)
    time.sleep(0.5)
    Servo.stop()

  #左まわり　開ける
  def move_open(self):
    Servo = GPIO.PWM(17, 50)
    Servo.start(10.5)
    time.sleep(0.5)
    Servo.stop()
