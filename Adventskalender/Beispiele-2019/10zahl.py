#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

seg={'a':21, 'b':8, 'c':11, 'd':26, 'e':19, 'f':20, 'g':13}
for s in "abcdefg":
  GPIO.setup(seg[s], GPIO.OUT, initial=0)

zif=[16, 12, 7, 6]
for z in zif:
  GPIO.setup(z, GPIO.OUT, initial=1)

zahl=[
  "abcdef",  #0
  "bc",      #1
  "abdeg",   #2
  "abcdg",   #3
  "bcfg",    #4
  "acdfg",   #5
  "acdefg",  #6
  "abc",     #7
  "abcdefg", #8
  "abcdfg",  #9
    ]

print("Strg+C beendet das Programm")
try:
  while True:
    for i in range(4):
      for s in "abcdefg":
        GPIO.output(seg[s], 0)
      GPIO.output(zif[i], 0)
      for s in zahl[i+1]:
        GPIO.output(seg[s], 1)
      time.sleep(0.001)
      GPIO.output(zif[i], 1)

except KeyboardInterrupt:
  GPIO.cleanup()
