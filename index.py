#!/bin/env python
# coding: utf-8
import json
from bottle import route, run, request, HTTPResponse, template, static_file
import RPi.GPIO as GPIO
import atexit
import time
import piServo

GPIO_PORT_LED_0 = 18

@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')

@route('/')
def root():
    return template("index")

# curl -H "Accept: application/json" -H "Content-type: application/json" -X POST -d '{"num":"0", "onoff":true}' http://192.168.1.88:8080/setLed
@route('/setLed', method='POST')
def setLedEntry():
    #var = request.json
    #GPIO.output(GPIO_PORT_LED_0, 1)
    print('POST完了')
    piservo = piServo.pi_servo()
    piservo.moveRight()
     #GPIO.output(GPIO_PORT_LED_0, 0)
    retBody = {"ret": "ok"}
    r = HTTPResponse(status=200, body=retBody)
    r.set_header('Content-Type', 'application/json')
    return r

def main():
    print("Initialize port")
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GPIO_PORT_LED_0, GPIO.OUT)
    GPIO.output(GPIO_PORT_LED_0, 0)

    print('Server Start')
    run(host='0.0.0.0', port=8080, debug=True, reloader=True)
    # run(host='0.0.0.0', port=8080, debug=False, reloader=False)

def atExit():
    print("atExit")
    GPIO.cleanup()

if __name__ == '__main__':
    atexit.register(atExit)
    main()