#!/usr/bin/python
import RPi.GPIO as GPIO
import time, datetime

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

taste1=18
GPIO.setup(taste1, GPIO.IN, GPIO.PUD_DOWN)
taste2=4
GPIO.setup(taste2, GPIO.IN, GPIO.PUD_DOWN)

z=[0,0,0,0]

def za():
  for i in range(4):
    for s in "abcdefg":
      GPIO.output(seg[s], 0)
    GPIO.output(zif[i], 0)
    for s in zahl[z[i]]:
      GPIO.output(seg[s], 1)
    time.sleep(0.001)
    GPIO.output(zif[i], 1)

print("Zum Start des Countdowns und zum Neustart Taste 1 drücken")
print("Zum Beenden Taste 2 drücken")
while True:
  t=datetime.date(2019, 12, 24) - datetime.date.today()
  x=t.days
  z[0]=int(x/1000)
  z[1]=int(x%1000/100)
  z[2]=int(x%100/10)
  z[3]=int(x%10)
  if GPIO.input(taste2)==1:
    break

  while GPIO.input(taste1)==0:
    za()
    if GPIO.input(taste2)==1:
      break

  while x>=0:
    z[0]=int(x/1000)
    z[1]=int(x%1000/100)
    z[2]=int(x%100/10)
    z[3]=int(x%10)
    for j in range(100):
      za()
    x-=1
    if GPIO.input(taste2)==1:
      break

  while GPIO.input(taste1)==0:
    za()
    if GPIO.input(taste2)==1:
      break

GPIO.cleanup()
