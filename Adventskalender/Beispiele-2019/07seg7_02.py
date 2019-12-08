#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

seg={'c':11, 'd':26, 'e':19, 'g':13}
for s in "cdeg":
  GPIO.setup(seg[s], GPIO.OUT, initial=0)

print("Strg+C beendet das Programm")
try:
  while True:
    for s in "cdeg":
      GPIO.output(seg[s], 1)
      time.sleep(0.1)
      GPIO.output(seg[s], 0)

except KeyboardInterrupt:
  GPIO.cleanup()
