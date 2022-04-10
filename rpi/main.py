import RPi.GPIO as GPIO 
from gpiozero import Servo
import time  
import cv2
from time import sleep
 
from pred import predict
from upload_image import upload_image

from gpiozero.pins.pigpio import PiGPIOFactory

factory = PiGPIOFactory()

GPIO.setmode(GPIO.BCM)
 
servorotate = Servo(17, pin_factory=factory)
servodrop = Servo(18, pin_factory=factory) 
 
INSIDE_LED = 4

GREEN_LED = 22
 
GPIO.setup(INSIDE_LED, GPIO.OUT) 

GPIO.setup(GREEN_LED, GPIO.OUT)
 
start_time = time.time()
state = 'idle'

GPIO.output(INSIDE_LED, GPIO.LOW)

GPIO.output(GREEN_LED, GPIO.HIGH)

servorotate.value = 1
servodrop.value = 0

cap = cv2.VideoCapture(0)

def movemotor(result):
    #if result == 'hazard':
     #   GPIO.output(RED_LED, GPIO.LOW) # red led
    #else:
    #GPIO.output(GREEN_LED, GPIO.HIGH) # green led

    print(f"FINAL MOTOR TURN: {result}")

    if result == 'trash':
        GPIO.output(GREEN_LED, GPIO.LOW) # green led
        servorotate.value = 1
        servodrop.value = -0.9
        
    elif result == 'recycle':
        GPIO.output(GREEN_LED, GPIO.LOW) # green led
        servorotate.value = 0
        servodrop.value = 0
        
    elif result == 'compost':
        GPIO.output(GREEN_LED, GPIO.LOW) # green led
        servorotate.value = 1
        servodrop.value = 0.9
 
    sleep(3) # pause program
    
    GPIO.output(GREEN_LED, GPIO.HIGH) # green led
 
    servorotate.value = 1
    servodrop.value = 0
 


sleep(3)

while True:
    
    GPIO.output(INSIDE_LED, GPIO.HIGH)
    sleep(1)
    ret, frame = cap.read()
    
    sleep(1)
    
    GPIO.output(INSIDE_LED, GPIO.LOW)   
    
    # prediction
    result = predict(frame)
    print(result)
 
    if state == 'idle' and result != 'none':
        start_time = time.time()
        state = 'detect'
 
    if state == 'detect':
        if time.time() - start_time > 5:
            state = 'idle'
            
            if result=='none':
                continue
                
            cv2.imwrite('image.jpg', frame)
            sleep(0.5)
            upload_image('image.jpg', result)
            sleep(0.5)
            
            movemotor(result)
 
GPIO.output(INSIDE_LED, GPIO.HIGH)

