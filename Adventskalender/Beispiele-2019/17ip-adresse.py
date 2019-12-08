#!/usr/bin/python
import RPi.GPIO as GPIO
import time, os

GPIO.setmode(GPIO.BCM)

seg={'a':21, 'b':8, 'c':11, 'd':26, 'e':19, 'f':20, 'g':13}
for s in "abcdefg":
  GPIO.setup(seg[s], GPIO.OUT, initial=0)

zif=[16, 12, 7, 6]
for z in zif:
  GPIO.setup(z, GPIO.OUT, initial=1)

dp = 5
GPIO.setup(dp, GPIO.OUT, initial=0)

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

z = [0,0,0]
ip = os.popen("hostname -I").readline()[:-2].split(".")

print("Strg+C beendet das Programm")

def za():
    for i in range(3):
      for s in "abcdefg":
        GPIO.output(seg[s], 0)
      GPIO.output(zif[i], 0)
      for s in zahl[z[i]]:
        GPIO.output(seg[s], 1)
      time.sleep(0.001)
      GPIO.output(zif[i], 1)

def blink():
    for s in "abcdefg":
      GPIO.output(seg[s], 0)
    for k in range(3):
      GPIO.output(zif[k], 0)
    GPIO.output(dp, 1)
    time.sleep(0.5)
    GPIO.output(dp, 0)

try:
  while True:
    for j in ip:
      for k in range(3):
        z[k] = int(j.zfill(3)[k])
      sek = time.time()
      while time.time() <= sek + 1:
        za()
    blink()

except KeyboardInterrupt:
  GPIO.cleanup()
