import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

def off():
	print "Turning off.."
	GPIO.output(17, False)
	print "Turned off"

off()
