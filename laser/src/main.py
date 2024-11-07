import RPi.GPIO as GPIO
import time


laser_pin = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(laser_pin, GPIO.OUT)

GPIO.output(laser_pin, GPIO.HIGH)
time.sleep(5)
GPIO.output(laser_pin, GPIO.LOW)