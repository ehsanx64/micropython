# ADC (Analog to Digital Conversion)

from machine import ADC

# ESP8266 has only one ADC channel

adc = ADC(0)        # Create ADC object on ADC pin
val = adc.read()    # Read the value which is in 0 - 1024 range
