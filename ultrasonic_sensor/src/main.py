import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

TRIG=23
ECHO=24

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def get_distance():
    GPIO.output(TRIG, GPIO.LOW)
    time.sleep(2)
    GPIO.output(TRIG, GPIO.HIGH)
    time.sleep(1e-5)
    GPIO.output(TRIG, GPIO.LOW)

    while GPIO.input(ECHO) == GPIO.LOW:
        pulse_start = time.time()

    while GPIO.input(ECHO) == GPIO.HIGH:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    return pulse_duration * 17150

while True:
    distance = get_distance()
    print(f"distance: {round(distance,2)}cm")
    time.sleep(1)