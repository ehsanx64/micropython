# Onboard LED

import machine

pin = machine.Pin(2, machine.Pin.OUT)

# Turn on the LED
def led_on():
    pin.off()

# Turn on the LED
def led_off():
    pin.on()

