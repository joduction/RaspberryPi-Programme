#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

rot    = 18
gelb   = 23
gruen  = 24

GPIO.setup(rot, GPIO.OUT, initial=0)
GPIO.setup(gelb, GPIO.OUT, initial=0)
GPIO.setup(gruen, GPIO.OUT, initial=1)

print("Strg+C beendet das Programm")

try:
    while True:
        time.sleep(2)
        GPIO.output(gruen,0)
        GPIO.output(gelb,1)
        time.sleep(0.6)
        GPIO.output(gelb,0)
        GPIO.output(rot,1)
        time.sleep(2)
        GPIO.output(gelb,1)
        time.sleep(0.6)
        GPIO.output(rot,0)
        GPIO.output(gelb,0)
        GPIO.output(gruen,1)

except KeyboardInterrupt:
    GPIO.cleanup()
