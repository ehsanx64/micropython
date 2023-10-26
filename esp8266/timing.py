# Delay and timing

import time

# Sleep for 1 second
time.sleep(1)

# Sleep for 500 milliseconds
time.sleep_ms(500)

# Sleep for 10 microseconds
time.sleep_us(10)

# Save current millisecond timer (tick) value
start = time.ticks_ms()
time.sleep_ms(100)
# Compute the delta (difference)
delta = time.ticks_diff(time.ticks_ms(), start)

print("Delta:", delta)