import RPi.GPIO as GPIO
import time

redPin = 18 
yellowPin = 22
greenPin = 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(redPin, GPIO.OUT)
GPIO.setup(yellowPin, GPIO.OUT)
GPIO.setup(greenPin, GPIO.OUT)

def blink(numTimes, speed):
    for i in range(0,numTimes):
        print "Iteration " + str(i+1)
        GPIO.output(redPin, True)
        time.sleep(speed)
        GPIO.output(redPin, False)
        time.sleep(speed)
	GPIO.output(yellowPin, True)
	time.sleep(speed)
	GPIO.output(yellowPin, False)
	time.sleep(speed)
	GPIO.output(greenPin, True)
	time.sleep(speed)
	GPIO.output(greenPin, False)
	time.sleep(speed)
    print "Finished"
    GPIO.cleanup()

# User input
iterations = raw_input("Enter the total number of times to blink: ")
speed = raw_input("Enter the length of each blink in seconds: ")

# Start function and pass given arguments
blink(int(iterations),float(speed))

