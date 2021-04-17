#	References:
#		DIY Dupont Connectors
#			https://www.youtube.com/watch?v=N3zK9fzIPBo
#	   http://www.pibits.net/amp/code/ky-003-hall-magnetic-sensor-module-and-raspberry-pi.php

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

sensor = 4
led = 27
GPIO.setup(sensor, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
# GPIO.setup(PIR_sensor, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)		#	10/28/2020

# GPIO.setup(led, GPIO.OUT)


#Function executed on signal detection
def active(pin):
	# GPIO.out(led,GPIO.HIGH)
	print('Action')
	v = GPIO.input(pin)
	print("pin %s's value is %s" % (pin, v ))


#On detecting signal (falling edge), active function will be activated.
GPIO.add_event_detect(sensor, GPIO.RISING, callback=active, bouncetime=100)
# GPIO.add_event_detect(PIR_sensor, GPIO.RISING, callback=active, bouncetime=100)

# main program loop
try:
		while True:
			print( GPIO.input( sensor ))
			time.sleep(.1)

# Scavenging work after the end of the program
except KeyboardInterrupt:
        GPIO.cleanup()
