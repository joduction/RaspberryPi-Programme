#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

seg=[21, 13, 26]
for s in range(3):
  GPIO.setup(seg[s], GPIO.OUT, initial=0)

print("Strg+C beendet das Programm")
try:
  while True:
    for i in range(3):
      GPIO.output(seg[i], 1)
      time.sleep(0.2)
      GPIO.output(seg[i], 0)

except KeyboardInterrupt:
  GPIO.cleanup()
    
