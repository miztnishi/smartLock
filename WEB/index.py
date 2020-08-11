#!/bin/env python
# coding: utf-8
import json
from bottle import route, run, request, HTTPResponse, template, static_file
import RPi.GPIO as GPIO
import atexit
import time
import pi_servo
import send_line


@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')

@route('/')
def root():
    return template("index")

@route('/openDoor', method='POST')
def open_door():
    sendline = send_line.SendLine()
    try:
        piservo = pi_servo.PiServo()
        piservo.move_open()
        sendline.send("アプリからドアを開けました")
        retBody = {"ret": "ok"}
        r = HTTPResponse(status=200, body=retBody)

    except Exception as e:
        errMsg = "異常終了です:" + str(e)
        sendline.send(errMsg)
        retBody = {"ret": "NG:" + str(e)}
        r = HTTPResponse(status=500, body=retBody)

    r.set_header('Content-Type', 'application/json')
    return r

@route('/closeDoor', method='POST')
def open_door():
    sendline = send_line.SendLine()
    try:
        piservo = pi_servo.PiServo()
        piservo.move_close()
        sendline.send("アプリからドアを閉めました")
        retBody = {"ret": "ok"}
        r = HTTPResponse(status=200, body=retBody)

    except Exception as e:
        errMsg = "異常終了です:" + str(e)
        sendline.send(errMsg)
        retBody = {"ret": "NG:" + str(e)}
        r = HTTPResponse(status=500, body=retBody)

    r.set_header('Content-Type', 'application/json')
    return r



def main():
    print("Initialize port")
    GPIO.setmode(GPIO.BCM)
    print('Server Start')
    run(host='0.0.0.0', port=8080, debug=True, reloader=True)
    # run(host='0.0.0.0', port=8080, debug=False, reloader=False)

def atExit():
    print("atExit")
    GPIO.cleanup()

if __name__ == '__main__':
    atexit.register(atExit)
    main()