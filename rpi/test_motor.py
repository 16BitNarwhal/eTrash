import RPi.GPIO as GPIO


import time  
from time import sleep

from gpiozero import Servo

from gpiozero.pins.pigpio import PiGPIOFactory

factory = PiGPIOFactory()

servo = Servo(17, pin_factory=factory)
servo1 = Servo(18, pin_factory=factory)



GPIO.setmode(GPIO.BCM)
 
INSIDE_LED = 4 #gpio 4, pin 7
RED_LED = 27 #gpio 27, pin 13
GREEN_LED = 22 #gpio 22, pin 15
	
GPIO.setup(INSIDE_LED, GPIO.OUT) 
GPIO.setup(RED_LED, GPIO.OUT)
GPIO.setup(GREEN_LED, GPIO.OUT)
 
GPIO.output(INSIDE_LED, GPIO.LOW)
GPIO.output(RED_LED, GPIO.HIGH) 	 
GPIO.output(GREEN_LED, GPIO.HIGH)  



servo1.value = -0.1
servo.value = 1

sleep(10)


servo1.value = -1
servo.value = 1

sleep(10)

servo1.value = -0.1
servo.value = 1

sleep(10)          


servo1.value = 1                                                                                                           
servo.value = 1

sleep(10)


servo1.value = -0.1
servo.value = 1

sleep(10)                                                  





servo.value = None
