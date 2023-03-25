import RPi.GPIO as gpio
import wiringpi2 as wp
import time
print(gpio.RPI_INFO)
gpio.setmode(gpio.BOARD)
wp.wiringPiSetupGpio()
pin = 32
gpio.setup(pin,gpio.OUT)
pwm = gpio.PWM(pin,440)
while(True):    
    pwm.start(40)
