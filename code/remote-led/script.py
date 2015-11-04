# This script will fetch the current state of color and try to set it
# The GPIO hasnt been implemented yet

import RPi.GPIO as GPIO
import urllib2
import time

redPin = None
bluePin = None
greenPin = None

GPIO.setmode(GPIO.BCM)
GPIO.setup(redPin, GPIO.OUT)
GPIO.setup(bluePin, GPIO.OUT)
GPIO.setup(greenPin, GPIO.OUT)

def fetch():
	# do stuff 
	data = urllib2.urlopen("http://manuelgu.eu/rpi/color.txt")
	for line in data:
		# line is equal the value
		
		if line == 'red':
			# set color to red
			print "Yay, red!"
		elif line == 'blue':
			# set color to blue
			print "Yay, blue!"
		elif line == 'green':
			# set color to green
			print "Yay, green!"
		elif line == 'stop':
			# turn all LEDs off
			print "Aww, no colors!"
		else:
			print "Something went wrong.."

	time.sleep(0.1)


while True:
	fetch()

