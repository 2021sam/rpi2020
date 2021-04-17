# http://www.raspblocks.com/rgb.html

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
# GPIO.setup(17, GPIO.OUT)
# GPIO.setup(27, GPIO.OUT)
# GPIO.setup(22, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)




PWMR1=GPIO.PWM(5,100);
PWMG1=GPIO.PWM(6,100);
PWMB1=GPIO.PWM(13,100);
PWMR1.start(100)
PWMG1.start(100)
PWMB1.start(100)
while True:
    PWMR1.ChangeDutyCycle(0)
    PWMG1.ChangeDutyCycle(100)
    PWMB1.ChangeDutyCycle(100)
    time.sleep(1)
    PWMR1.ChangeDutyCycle(80)
    PWMG1.ChangeDutyCycle(20)
    PWMB1.ChangeDutyCycle(100)
    time.sleep(1)
    PWMR1.ChangeDutyCycle(80)
    PWMG1.ChangeDutyCycle(80)
    PWMB1.ChangeDutyCycle(0)
    time.sleep(1)
    PWMR1.ChangeDutyCycle(0)
    PWMG1.ChangeDutyCycle(20)
    PWMB1.ChangeDutyCycle(100)
    time.sleep(1)
