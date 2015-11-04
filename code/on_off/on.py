import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

def on():
	print "Turning on.."
	GPIO.output(17, True)
	print "Turned on"

on()
