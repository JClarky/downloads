import RPi.GPIO as GPIO

########## GPIO Setup
GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

pin_motor_left = 20
pin_motor_right = 21

GPIO.setup(pin_motor_left, GPIO.OUT)
GPIO.setup(pin_motor_right, GPIO.OUT)

l = GPIO.PWM(pin_motor_left, 500) 
l.start(0)

r = GPIO.PWM(pin_motor_right, 500) 
r.start(0)

#pf.ChangeDutyCycle(l)

while True:
    l.ChangeDutyCycle(int(input("Left motor: ")))
    r.ChangeDutyCycle(int(input("Right motor: ")))