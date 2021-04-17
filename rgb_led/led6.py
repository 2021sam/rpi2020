# pip install rpi.gpio
import time
import RPi.GPIO as GPIO
# Pin definitions
pin1	= 17
pin2	= 22
pin3	= 27
pin4	= 18
# Suppress warnings
GPIO.setwarnings(False)
# Use "GPIO" pin numbering
GPIO.setmode(GPIO.BCM)
# Set LED pin as output
GPIO.setup(pin1, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)
GPIO.setup(pin3, GPIO.OUT)
GPIO.setup(pin4, GPIO.OUT)

# Blink forever
GPIO.output(pin1, GPIO.HIGH) # Turn LED on
GPIO.output(pin2, GPIO.HIGH) # Turn LED on
GPIO.output(pin3, GPIO.HIGH) # Turn LED on

while True:
	print('HIGH')
	GPIO.output(pin4, GPIO.HIGH)
	time.sleep(3)                   # Delay for 1 second
	# GPIO.output(pin1, GPIO.LOW)  # Turn LED off
	# GPIO.output(pin2, GPIO.LOW)  # Turn LED off
	# GPIO.output(pin3, GPIO.LOW)  # Turn LED off
	print('LOW')
	GPIO.output(pin4, GPIO.LOW)
	# GPIO.cleanup()
	time.sleep(10)                   # Delay for 1 second
