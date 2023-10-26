# PWM (Pulse Width Modulation)

from machine import Pin, PWM
import time

pwm = PWM(Pin(2))

# Print current frequency
print("Initial frequency:", pwm.freq())

# Set frequency
pwm.freq(1000)

# Print duty cycle
print("Initial duty cycle:", pwm.duty())

# Set duty cycle
pwm.duty(1023)

for i in range(0, 1023):
    print(i)
    pwm.duty(i)
    time.sleep_ms(1)
    
