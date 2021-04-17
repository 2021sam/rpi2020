# https://www.instructables.com/Raspberry-Pi-3-RGB-LED-With-Using-PWM/
# https://www.evilmadscientist.com/2012/resistors-for-leds/

#defining the RPi's pins as Input / Output
import RPi.GPIO as GPIO

#importing the library for delaying command.
import time

#used for GPIO numbering
GPIO.setmode(GPIO.BCM)

#closing the warnings when you are compiling the code
GPIO.setwarnings(False)

RUNNING = True

#defining the pins
# green = 20
# red = 21
# blue = 22

# green = 17
# red = 27
# blue = 22

# green = 22
# red = 17
# blue = 27


green = 27
red = 22
blue = 17
SLEEP_TIME = 5


#defining the pins as output
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

#choosing a frequency for pwm
Freq = 100

#defining the pins that are going to be used with PWM
RED = GPIO.PWM(red, Freq)
GREEN = GPIO.PWM(green, Freq)
BLUE = GPIO.PWM(blue, Freq)

try:
	#we are starting with the loop
	# while RUNNING:
		#lighting up the pins. 100 means giving 100% to the pin
	#For anode RGB LED users, if you want to start with RED too the only thing to be done is defining RED as one and GREEN and BLUE as 100.

	print( 'Red')
	RED.start(1)
	GREEN.start(100)
	BLUE.start(100)
	# RED.ChangeDutyCycle(1)
	# GREEN.ChangeDutyCycle(100)
	# BLUE.ChangeDutyCycle(100)
	time.sleep( SLEEP_TIME )

	print( 'Green')
	# RED.start(100)
	# GREEN.start(1)
	# BLUE.start(100)
	RED.ChangeDutyCycle(100)
	GREEN.ChangeDutyCycle(1)
	BLUE.ChangeDutyCycle(100)
	time.sleep( SLEEP_TIME )


	print( 'Blue')
	RED.start(100)
	GREEN.start(100)
	BLUE.start(1)
	# RED.ChangeDutyCycle(100)
	# GREEN.ChangeDutyCycle(100)
	# BLUE.ChangeDutyCycle(1)
	time.sleep( SLEEP_TIME )




except KeyboardInterrupt:
# the purpose of this part is, when you interrupt the code, it will stop the while loop and turn off the pins, which means your LED won't light anymore
	RUNNING = False
	GPIO.cleanup()
