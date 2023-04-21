import time
import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)
gpio.setup(18, gpio.OUT)

