# Hardware-related functions

import esp
import machine
import os
import micropython

def info():
    # Print firmware info
    print("Firmware:  ")
    esp.check_fw()

    # Display some important info
    print("Dir. List: ", os.listdir())
    print("MCU Freq.: ", machine.freq())
    print("Mem. info: ", micropython.mem_info())
    print("Mem. ESP:  ", str(esp.freemem()))
    print("Stack info:", micropython.stack_use())