#!/usr/bin/python
import RPi.GPIO as GPIO
import time, random

GPIO.setmode(GPIO.BCM)

seg={'a':21, 'b':8, 'c':11, 'd':26, 'e':19, 'f':20, 'g':13}
for s in "abcdefg":
  GPIO.setup(seg[s], GPIO.OUT, initial=0)

zif=[16, 12, 7, 6]
for z in zif:
  GPIO.setup(z, GPIO.OUT, initial=1)

dp=5
GPIO.setup(dp, GPIO.OUT, initial=0)

LED1=24
GPIO.setup(LED1, GPIO.OUT, initial=0)
LED2=23
GPIO.setup(LED2, GPIO.OUT, initial=0)

t1=18
t2=17
t3=4
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

z=[0,0,0,0]
x=0

print("Taste 1 verringert den Tipp")
print("Taste 2 erhöht den Tipp")
print("Taste 3 gibt den Tipp ab")
print("Strg+C beendet das Programm")

def za(n):
  z[0] = int(n / 1000)
  z[1] = int(n % 1000 / 100)
  z[2] = int(n % 100 / 10)
  z[3] = int(n % 10)
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
    y=random.randrange(100)
    t=0
    while True:
      za(x * 100 + t)
      if GPIO.input(t1)==1 and x>0:
        x-=1
        time.sleep(0.08)
      if GPIO.input(t2)==1 and x<99:
        x+=1
        time.sleep(0.08)
      if GPIO.input(t3)==1:
        t+=1
        if y<x:
          GPIO.output(LED1, 1)
          time.sleep(0.5)
          GPIO.output(LED1, 0)
        if y>x:
          GPIO.output(LED2, 1)
          time.sleep(0.5)
          GPIO.output(LED2, 0)
        if y==x:
          for i in range(5):
            GPIO.output(LED1, 1)
            GPIO.output(LED2, 1)
            for j in range(100):
              za(x * 100 + t)
            GPIO.output(LED1, 0)
            GPIO.output(LED2, 0)
            for j in range(100):
              za(x * 100 + t)
          break

except KeyboardInterrupt:
  GPIO.cleanup()
