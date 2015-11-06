# This script will fetch the current state of color and try to set it
# Additionally it will tell you the current color using TTS

import RPi.GPIO as GPIO
import urllib2
import time
import subprocess

redPin = 18
yellowPin = 22
greenPin = 12

sayColor = True

current = "nothing"

GPIO.setmode(GPIO.BCM)
GPIO.setup(redPin, GPIO.OUT)
GPIO.setup(yellowPin, GPIO.OUT)
GPIO.setup(greenPin, GPIO.OUT)

subprocess.call('./saybooting.sh')

def fetch():
	# do stuff 
	data = urllib2.urlopen("http://manuelgu.eu/rpi/remote-led/color.txt")
	for line in data:
		# line is equal the value
		
		if line == 'red':
			# set color to red
			global current
			if current != line:
				
				print "Yay, red!"
				empty()
				GPIO.output(redPin, True)
				if sayColor:
					subprocess.call('./sayred.sh')
				current = line
		elif line == 'yellow':
			# set color to yellow
			global current
			if current != line:

				print "Yay, yellow!"
				empty()
				GPIO.output(yellowPin, True)
				if sayColor:
					subprocess.call('./sayyellow.sh')
				current = line
		elif line == 'green':
			# set color to green
			global current
			if current != line:

				print "Yay, green!"
				empty()
				GPIO.output(greenPin, True)
				if sayColor:
					subprocess.call('./saygreen.sh')
				current = line
		elif line == 'stop':
			# turn all LEDs off
			global current
			if current != line:

				print "Aww, no colors!"
				empty()
				if sayColor:
					subprocess.call('./saystop.sh')
				current = line
		else:
			print "Something went wrong.."
			if sayColor:
				subprocess.call('./saywrong.sh')
			empty()
			current = "nothing"
	time.sleep(0.2)

def empty():
	GPIO.output(redPin, False)
	GPIO.output(yellowPin, False)
	GPIO.output(greenPin, False)

while True:
	fetch()
