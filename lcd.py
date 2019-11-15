# -*- coding: utf-8 -*-

import RPi.GPIO as gpio
import time

# pins = [21,26,20]
# lcdPins = [16,19,13,12]
namedPins = { # BCM
    'RS': 21,
    'RW': 26,
    'EN': 20,
}

digitalPins = [
    16,19,13,12
] 

def set_on_pin(pin, power):
    gpio.output(pin, gpio.HIGH if power else gpio.LOW)

def set_low(pin):
    gpio.output(pin, gpio.LOW)

def set_high(pin):
    gpio.output(pin, gpio.HIGH)

def set_line(bits):
    for i in range(4):
        set_on_pin(digitalPins[i], bits[i])

def send(byte):
    time_to_sleep = 0.1
    set_low(namedPins["RS"])
    set_low(namedPins["EN"])
    set_line([0,0,1,0])
    set_high(namedPins["EN"])
    time.sleep(time_to_sleep)
    set_low(namedPins["EN"]) #6
    time.sleep(time_to_sleep)
    set_line([1,0,0,0])
    set_high(namedPins["EN"])
    time.sleep(time_to_sleep)
    set_low(namedPins["EN"]) 
    time.sleep(time_to_sleep)


def clear():
    send(0b00000001)

def cursorToHome():
    send(0b00000010)

def cursorToHome():
    send(0b00000010)

def init():
    gpio.setmode(gpio.BCM)                 
    
    for pin in namedPins.values():
        gpio.setup(pin, gpio.OUT)

    for pin in digitalPins:
        gpio.setup(pin, gpio.OUT)



def show_char(char):
    pass


def foo(halfByte): # 4 цифры
    gpio.output(pins['RS'], gpio.LOW)
    gpio.output(pins['EN'], gpio.LOW)

    for pin in lcdPins:
        gpio.output(pin, gpio.HIGH)

