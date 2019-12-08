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

z = [0,0,0,0]
print("Strg+C beendet das Programm")

def za():
  for i in range(4):
    for s in "abcdefg":
      GPIO.output(seg[s], 0)
    GPIO.output(zif[i], 0)
    for s in zahl[z[i]]:
      GPIO.output(seg[s], 1)
    if i == 1:
      GPIO.output(dp, 1)
    else:
      GPIO.output(dp, 0)
    time.sleep(0.001)
    GPIO.output(zif[i], 1)

try:
  while True:
    zeit = time.localtime()
    h = zeit.tm_hour
    m = zeit.tm_min
    z[0] = int(h / 10)
    z[1] = h % 10
    z[2] = int(m / 10)
    z[3] = m % 10
    while time.localtime().tm_min == m:
      za()

except KeyboardInterrupt:
  GPIO.cleanup()
