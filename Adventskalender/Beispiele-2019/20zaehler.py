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

dp=5
GPIO.setup(dp, GPIO.OUT, initial=0)

k1=17
k2=4
GPIO.setup(k1, GPIO.IN)
GPIO.setup(k2, GPIO.IN)

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

print("Sensorkontakt 1 erhöht die Zahl")
print("Sensorkontakt 2 verringert die Zahl")
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
    time.sleep(0.001)
    GPIO.output(zif[i], 1)

try:
  while True:
    za(x)
    if GPIO.input(k1)==0 and x>0:
      x-=1
    if GPIO.input(k2)==0 and x<9999:
      x+=1

except KeyboardInterrupt:
  GPIO.cleanup()
