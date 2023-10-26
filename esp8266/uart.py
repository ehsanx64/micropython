# UART (serial bus)

from machine import UART

# Use UART channel 0 with baudrate of 115200
uart = UART(0, baudrate=115200)

# Print a string
uart.write('hello\n')

# Read up to 5 characters and print it
i = uart.read(5)
print("Input:", i)
