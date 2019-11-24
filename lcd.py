# -*- coding: utf-8 -*-

import RPi.GPIO as gpio
import time

# pins = [21,26,20]
# lcdPins = [16,19,13,12]
namedPins = {  # BCM
    'RS': 21,
    'RW': 26,
    'EN': 20,
}

digitalPins = [
    16, 19, 13, 12
]


def set_on_pin(pin, power):
    gpio.output(pin, gpio.HIGH if power else gpio.LOW)


def set_low(pin):
    gpio.output(pin, gpio.LOW)


def set_high(pin):
    gpio.output(pin, gpio.HIGH)


def set_line(bits):
    for i in range(len(digitalPins)):
        set_on_pin(digitalPins[i], bits[i])


def send(byte):
    bits = byte_to_bits(byte)
    time_to_sleep = 0.1
    set_low(namedPins["EN"])
    set_line(bits[0:4])
    set_high(namedPins["EN"])
    time.sleep(time_to_sleep)
    set_low(namedPins["EN"])
    set_line(bits[4:8])
    set_high(namedPins["EN"])
    time.sleep(time_to_sleep)
    set_low(namedPins["EN"])


def send_command(command):
    set_high(namedPins["RS"])
    send(command)
    set_low(namedPins["RS"])


def byte_to_bits(byte):
    bits = []
    for i in range(8):
        bits.append(byte & 1)
        byte >>= 1
    bits.reverse()
    return bits


def clear():
    send(0b00000001)


def cursor_to_home():
    send(0b00000010)


def init():
    gpio.setmode(gpio.BCM)

    for pin in namedPins.values():
        gpio.setup(pin, gpio.OUT)

    for pin in digitalPins:
        gpio.setup(pin, gpio.OUT)

    send_command(0b00101000)


def show_char(char):
    send(ord(char))


def show_line(string):
    for char in string:
        show_char(char)
