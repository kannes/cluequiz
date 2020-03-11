# Clue quiz
# Copyright (C) 2018-2020  Luca Schmid

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import serial
from pygame.key import get_pressed
from pygame.locals import K_1, K_2, K_3, K_4
import RPi.GPIO as GPIO

gpio = 4
gpio4o = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(gpio, GPIO.IN)
GPIO.setup(gpio4o, GPIO.OUT)

gpio_button_red = 4
gpio_button_green = 22
gpio_button_blue=13
gpio_button_yellow=26
gpio_led_red = 17
gpio_led_green = 27
gpio_led_blue=5
gpio_led_yellow=19

GPIO.setmode(GPIO.BCM)
GPIO.setup(gpio, GPIO.IN)
GPIO.setup(gpio4o, GPIO.OUT)

GPIO.setup(gpio_button_red, GPIO.IN)
GPIO.setup(gpio_led_red, GPIO.OUT)
GPIO.setup(gpio_button_green, GPIO.IN)
GPIO.setup(gpio_led_green, GPIO.OUT)
GPIO.setup(gpio_button_blue, GPIO.IN)
GPIO.setup(gpio_led_blue, GPIO.OUT)
GPIO.setup(gpio_button_yellow, GPIO.IN)
GPIO.setup(gpio_led_yellow, GPIO.OUT)

def open_serial(port, baud):
    try:
        return serial.Serial(port, baud, timeout=0)
    except serial.SerialException:
        return None

class Serial:
    def __init__(self, port, baud):
        self.port = port
        self.baud = baud
        self.serial = open_serial(port, baud)

    def keep_alive(self):
        if not self.serial:
            self.serial = open_serial(self.port, self.baud)

    def read(self):
        if self.serial:
            try:
                return self.serial.read()
            except serial.SerialException:
                self.serial = None

        pressed = get_pressed()
        if pressed[K_1]:
            return b'1'
        elif pressed[K_2]:
            return b'2'
        elif pressed[K_3]:
            return b'3'
        elif pressed[K_4]:
            return b'4'
        elif GPIO.input(gpio_button_red):
#            GPIO.output(gpio_led_red, GPIO.HIGH) 
            return b'1'
        elif GPIO.input(gpio_button_green):
#            GPIO.output(gpio_led_green, GPIO.HIGH) 
            return b'2'            
        elif GPIO.input(gpio_button_blue):
#            GPIO.output(gpio_led_blue, GPIO.HIGH) 
            return b'3'
        elif GPIO.input(gpio_button_yellow):
#            GPIO.output(gpio_led_yellow, GPIO.HIGH) 
            return b'4'
        return b''
