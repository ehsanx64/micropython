# ESP8266 Demo

import esp
import machine
import os
import micropython

# Turn on the LED
pin = machine.Pin(2, machine.Pin.OUT)
pin.off()


# Print firmware info
esp.check_fw()

# Display some important info
print("Dir. List: ", os.listdir())
print("MCU Freq.: ", machine.freq())
print("Mem. info: ", micropython.mem_info())
print("Stack info:", micropython.stack_use())



