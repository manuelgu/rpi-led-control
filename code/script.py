#!/usr/bin/python

#import RPi.GPIO as GPIO
import urllib2
import time


def doTheThing():
	# do stuff 
	data = urllib2.urlopen("http://manuelgu.eu/rpi/color.txt")
	for line in data:
		# line is the value
		
		if line == 'red':
			# set color to red
			print "Yay, red!"
		elif line == 'blue':
			# set color to blue
			print "Yay, blue!"
		elif line == 'green':
			# set color to green
			print "Yay, green!"
		else:
			print "Something went wrong.."

	time.sleep(2)


while True:
	doTheThing()
