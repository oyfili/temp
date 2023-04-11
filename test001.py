#!/usr/bin/python3

import time
import dht11
import datetime  
from RPLCD.gpio import CharLCD
import RPi.GPIO as GPIO


# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# read data using pin 4
instance = dht11.DHT11(pin=4)

lcd = CharLCD(numbering_mode=GPIO.BOARD, cols=16, rows=2,
 pin_rs=37, pin_e=35,pin_e=35, pins_data=[33, 31, 29, 23],
 charmap='A02', auto_linebreaks=True, compat_mode=True)


try:
    while True:

        result = instance.read()
        if result.is_valid():
        print("Last valid input: " + str(datetime.datetime.now()))
        print("Temperature: %-3.1f C" % result.temperature)
        print("Humidity: %-3.1f %%" % result.humidity)

        lcd.clear()
        lcd.cursor_pos = (0, 0)
        lcd.write_string(""Temperature: %-3.1f C" % result.temperature")
        lcd.cursor_pos = (1, 0)
        lcd.write_string("Humidity: %-3.1f %%" % result.humidity)
        time.sleep(3)

except KeyboardInterrupt:
    print("Cleanup")
    GPIO.cleanup()