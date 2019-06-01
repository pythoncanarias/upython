import time
import machine


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


pin = [machine.Pin(14, machine.Pin.OUT),
       machine.Pin(12, machine.Pin.OUT),
       machine.Pin(13, machine.Pin.OUT)]

contador_ms = [CuentaMs(1000), CuentaMs(2333), CuentaMs(1698)]

while True:
    time.sleep(0.1)
    for i, e in enumerate(contador_ms):
        if e.comprueba():
            pin[i].value(not pin[i].value())
            print(" " * i, i, "ha pasado su tiempo")
