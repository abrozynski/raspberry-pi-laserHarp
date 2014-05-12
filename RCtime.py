#!/usr/bin/python

import RPi.GPIO as GPIO, time, os

DEBUG = 1
GPIO.setmode(GPIO.BOARD)

def RCtime(RCpin, max_reading=999999999):
 reading = 0
 GPIO.setup(RCpin, GPIO.OUT)
 GPIO.output(RCpin, GPIO.LOW)
 time.sleep(0.00001)

 GPIO.setup(RCpin, GPIO.IN)
 while (GPIO.input(RCpin) == GPIO.LOW):
  reading += 1
#  if reading > max_reading:
#    break
#  print reading
 return reading


#while True:
# print RCtime(12)
