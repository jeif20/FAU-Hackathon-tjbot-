import RPi.GPIO as GPIO
import time
from picamera import PiCamera
from time import sleep

GPIO.setmode(GPIO.BCM)

TRIG = 23
ECHO = 24

print "Distance Measurement In Progress"

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

GPIO.output(TRIG, False)
print "Waiting For Sensor To Settle"
time.sleep(2)

GPIO.output(TRIG, True)
time.sleep(0.00001)
GPIO.output(TRIG, False)

while GPIO.input(ECHO) ==0:
        pulse_start = time.time()

while GPIO.input(ECHO) ==1:
        pulse_end = time.time()

pulse_duration = pulse_end - pulse_start
distance = pulse_duration * 17150
distance = round(distance, 2)

if distance <= 25:
        camera = PiCamera()
        camera.start_preview()
        sleep(3)
        camera.capture('/home/pi/picture.jpg')
        camera.stop_preview()

GPIO.cleanup()