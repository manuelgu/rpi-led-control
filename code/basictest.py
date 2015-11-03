#!/usr/bin/python

# This is a very basic script that will make the LEDs blinking

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)

def blink(numTimes, speed):
    for i in range(0,numTimes):
        print "Iteration " + str(i+1)
        GPIO.output(7, True)
        time.sleep(speed)
        GPIO.output(7, False)
        time.sleep(speed)
    print "Finished"
    GPIO.cleanup()

# User input
iterations = raw_input("Enter the total number of times to blink: ")
speed = raw_input("Enter the length of each blink in seconds: ")

# Start function and pass given arguments
blink(int(iterations),float(speed))
