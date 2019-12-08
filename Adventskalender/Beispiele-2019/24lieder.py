#!/usr/bin/python
import RPi.GPIO as GPIO
import time, subprocess

GPIO.setmode(GPIO.BCM)

seg={'a':21, 'b':8, 'c':11, 'd':26, 'e':19, 'f':20, 'g':13}
for s in "abcdefg":
  GPIO.setup(seg[s], GPIO.OUT, initial=0)

zif=[16, 12, 7, 6]
for z in zif:
  GPIO.setup(z, GPIO.OUT, initial=1)

t1=23
t2=22
t3=27
t4=17
GPIO.setup(t1, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(t2, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(t3, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(t4, GPIO.IN, GPIO.PUD_DOWN)

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

def za(n):
  for s in "abcdefg":
    GPIO.output(seg[s], 0)
  for i in range(4):
    GPIO.output(zif[i], 1)
  if n!=0:      
    for s in zahl[n]:
      GPIO.output(seg[s], 1)
    GPIO.output(zif[n-1], 0)

try:
  while True:
    if GPIO.input(t1)==1:
      za(1)
      subprocess.Popen(["omxplayer", "lied1.mp3"])
      time.sleep(4)
      za(0)
    if GPIO.input(t2)==1:
      za(2)
      subprocess.Popen(["omxplayer", "lied2.mp3"])
      time.sleep(4)
      za(0)
    if GPIO.input(t3)==1:
      za(3)
      subprocess.Popen(["omxplayer", "lied3.mp3"])
      time.sleep(4)
      za(0)
    if GPIO.input(t4)==1:
      za(4)
      subprocess.Popen(["omxplayer", "lied4.mp3"])
      time.sleep(4)
      za(0)

except KeyboardInterrupt:
  GPIO.cleanup()
