import RPi.GPIO as GPIO
import time

# Setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
x = int(0)
pin = 26 # The GPIO Pin of the LED

# Output Definierung
GPIO.setup(pin, GPIO.OUT)

# How many times do the LED on and off?
x = int(input('Wie oft soll die LED blinken? '))


for i in range(x):
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(0.5)
