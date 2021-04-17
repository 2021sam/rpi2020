# https://thepihut.com/blogs/raspberry-pi-tutorials/27968772-turning-on-an-led-with-your-raspberry-pis-gpio-pins

import RPi.GPIO as GPIO
import time

LED = 22


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LED,GPIO.OUT)
print "LED on"
GPIO.output(LED,GPIO.HIGH)
time.sleep(1)
print "LED off"
GPIO.output(LED,GPIO.LOW)
