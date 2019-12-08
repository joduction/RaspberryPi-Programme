# Import
import RPi.GPIO as GPIO
import time as time

# Setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
x = int(0)

# Output Definierung
GPIO.setup(18, GPIO.OUT)

# Ende definieren
y = int(input('Wie oft soll die LED blinken? '))

# Program
while True:
    x = x + 1
    GPIO.output(18, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(18, GPIO.LOW)
    time.sleep(0.5)
    
    if(x == y):
        break
        