import time
import machine
""" dejamos el espacio de nombres sin "aplanar"
    es decir, NO hacemos:
    from machine import * """


class CuentaMs():
    def __init__(self, ms):
        self.ms = ms
        self.reset()

    def reset(self):
        self.proximo = time.ticks_ms() + self.ms

    def comprueba(self):
        if self.proximo <= time.ticks_ms():
            self.reset()
            return True
        else:
            return False


PIN_LED = 16    # puede cambiar en cada placa
led = machine.Pin(PIN_LED, machine.Pin.OUT)
contador_ms = CuentaMs(500)

while True:
    # hacemos el resto de tareas
    # ¿las insertamos aquí, o despues del if?
    if contador_ms.comprueba():
        led.value(not led.value())
