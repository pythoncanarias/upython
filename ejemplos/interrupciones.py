import machine


interruptCounter = 0
totalInterruptsCounter = 0


def callback(pin):
    global interruptCounter
    interruptCounter = interruptCounter+1
    led.value(not led.value())


p0 = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)
p0.irq(trigger=machine.Pin.IRQ_FALLING, handler=callback)

PIN_LED = 5     # puede cambiar en cada placa
led = machine.Pin(PIN_LED, machine.Pin.OUT)

while True:
    if interruptCounter > 0:
        state = machine.disable_irq()
        interruptCounter = interruptCounter-1
        machine.enable_irq(state)

        totalInterruptsCounter = totalInterruptsCounter+1
        print("Interrupt has occurred: " + str(totalInterruptsCounter))
