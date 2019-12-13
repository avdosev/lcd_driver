# -*- coding: utf-8 -*-

import RPi.GPIO as gpio
import time


RS = 21
EN  = 20

namedPins = [ RS, EN ]

D4 = 16
D5 = 19
D6 = 13
D7 = 12

digitalPins = [ D4, D5, D6, D7 ]
digitalPins.reverse()

LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line

TIME_TO_DELAY = 0.001


def set_on_pin(pin, power):
    gpio.output(pin, gpio.HIGH if power else gpio.LOW)


def set_low(pin):
    gpio.output(pin, gpio.LOW)


def set_high(pin):
    gpio.output(pin, gpio.HIGH)


def set_line(bits):
    for i in range(len(digitalPins)):
        set_on_pin(digitalPins[i], bits[i])


def send(byte, isCommand = False):
    set_on_pin(RS, not isCommand)
    bits = byte_to_bits(byte)
    
    set_line(bits[0:4])
    toggle()
    set_line(bits[4:8])
    toggle()
    

def toggle():
    time.sleep(TIME_TO_DELAY)
    set_high(EN)
    time.sleep(TIME_TO_DELAY)
    set_low(EN)
    time.sleep(TIME_TO_DELAY)


def send_command(command):
    send(command, True)


def byte_to_bits(byte):
    bits = []
    for i in range(8):
        bits.append(byte & 1)
        byte >>= 1
    bits.reverse()
    return bits


def clear():
    send_command(0b00000001)


def cursor_to_home():
    send_command(0b00000010)


def init():
    gpio.setwarnings(False)
    gpio.setmode(gpio.BCM)

    for pin in namedPins.values():
        gpio.setup(pin, gpio.OUT)

    for pin in digitalPins:
        gpio.setup(pin, gpio.OUT)

    send_command(0x33) # 110011 Initialise
    send_command(0x32) # 110010 Initialise
    send_command(0x06) # 000110 Cursor move direction
    send_command(0x0C) # 001100 Display On,Cursor Off, Blink Off
    send_command(0x28) # 101000 Data length, number of lines, font size
    send_command(0x01) # 000001 Clear display


def show_char(char):
    send(ord(char))


def show_line(string):
    for char in string:
        show_char(char)
        time.sleep(TIME_TO_DELAY)

def end():
    gpio.cleanup()
