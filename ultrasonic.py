##
# Ultrasonic library for MicroPython's machineoard.
# Compatible with HC-SR04 and SRF04.
#
# Copyright 2014 - Sergio Conde Gómez <skgsergio@gmail.com>
# Copyright 2017 - Lucas Grillo <jlucas.gl@gmail.com>
#                - Víctor Suárez García <suarez.garcia.victor@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Improved to ESP8266 with MicroPython
##

import machine
import time

# Pin configuration.
# WARNING: Do not use PA4-X5 or PA5-X6 as the echo pin without a 1k resistor.


class Ultrasonic:
    def __init__(self, tPin, ePin):
        self.triggerPin = tPin
        self.echoPin = ePin

        # Init trigger pin (out)
        self.trigger = machine.Pin(self.triggerPin)
        self.trigger.init(machine.Pin.OUT)
        self.trigger.off()

        # Init echo pin (in)
        self.echo = machine.Pin(self.echoPin)
        self.echo.init(machine.Pin.IN)

    def distance_in_inches(self):
        return (self.distance_in_cm() * 0.3937)

    def distance_in_cm(self):
        start = 0
        end = 0

        # Create a microseconds counter.
        start = time.ticks_us()

        # Send a 10us pulse.
        self.trigger.on()
        time.sleep_us(20)
        self.trigger.off()

        # Wait 'till whe pulse starts.
        while self.echo.value() == 0:
            start = time.ticks_us()

        # Wait 'till the pulse is gone.
        while self.echo.value() == 1:
            end = time.ticks_us()

        # Calc the duration of the recieved pulse, divide the result by
        # 2 (round-trip) and divide it by 29 (the speed of sound is
        # 340 m/s and that is 29 us/cm).
        dist_in_cm = ((end - start) / 2) / 29

        return dist_in_cm
