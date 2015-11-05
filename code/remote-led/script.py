# This script will fetch the current state of color and try to set it
# The GPIO hasnt been implemented yet

import RPi.GPIO as GPIO
import urllib2
import time

<<<<<<< HEAD
redPin = 18
yellowPin = 22
greenPin = 12
=======
redPin = None
yellowPin = None
greenPin = None
>>>>>>> origin/master

GPIO.setmode(GPIO.BCM)
GPIO.setup(redPin, GPIO.OUT)
GPIO.setup(yellowPin, GPIO.OUT)
GPIO.setup(greenPin, GPIO.OUT)

def fetch():
	# do stuff 
	data = urllib2.urlopen("http://manuelgu.eu/rpi/remote-led/color.txt")
	for line in data:
		# line is equal the value
		
		if line == 'red':
			# set color to red
			print "Yay, red!"
			empty()
			GPIO.output(redPin, True)
		elif line == 'yellow':
			# set color to yellow
			print "Yay, yellow!"
			empty()
			GPIO.output(yellowPin, True)
		elif line == 'green':
			# set color to green
			print "Yay, green!"
			empty()
			GPIO.output(greenPin, True)
		elif line == 'stop':
			# turn all LEDs off
			print "Aww, no colors!"
			empty()
		else:
			print "Something went wrong.."

	time.sleep(0.1)

def empty():
	GPIO.output(redPin, False)
<<<<<<< HEAD
	GPIO.output(yellowPin, False)
=======
	GPIO.output(bluePin, False)
>>>>>>> origin/master
	GPIO.output(greenPin, False)

while True:
	fetch()


