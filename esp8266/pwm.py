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

pwm.deinit()

def pulse():
    d = 0.0010
    
    for i in range(1024, 0, -1):
        pwm.duty(i)
        time.sleep(d)
    
    for i in range(0, 1024):
        pwm.duty(i)
        time.sleep(d)
    
for i in range(1, 5):
    pulse()

