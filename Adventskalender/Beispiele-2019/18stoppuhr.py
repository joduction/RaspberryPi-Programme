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

t1=22
t2=27
t3=17
GPIO.setup(t1, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(t2, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(t3, GPIO.IN, GPIO.PUD_DOWN)

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

print("Start: Taste 1")
print("Stopp: Taste 2")
print("Reset: Taste 3")
print("Strg+C beendet das Programm")

def za():
  for i in range(4):
    for s in "abcdefg":
      GPIO.output(seg[s], 0)
    GPIO.output(zif[i], 0)
    for s in zahl[z[i]]:
      GPIO.output(seg[s], 1)
    if i == 2:
      GPIO.output(dp, 1)
    else:
      GPIO.output(dp, 0)
    time.sleep(0.001)
    GPIO.output(zif[i], 1)

try:
  while True:
    z = [0,0,0,0]
    while GPIO.input(t1)==0:
      za()
    start = time.time()
    while GPIO.input(t2)==0:
      zeit = time.time() - start
      z[0] = int(zeit % 1000 / 100)
      z[1] = int(zeit % 100 / 10)
      z[2] = int(zeit % 10)
      z[3] = int(zeit * 10 % 10)
      while int((time.time() - start) * 10 % 10) == z[3]:
        za()
    while GPIO.input(t3)==0:
      za()

except KeyboardInterrupt:
  GPIO.cleanup()
