from machine import Pin
import time

button = Pin(2, Pin.IN)
led = Pin(16, Pin.OUT)

while True:
    state = button.value()
    led.value(state)
    time.sleep(0.5)
