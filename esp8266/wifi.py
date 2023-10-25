# WiFi

import network

# Create a station interface
sta = network.WLAN(network.STA_IF)

# Activate the interface
sta.active(True)

# Scan for access points
aps = sta.scan()

# Print the results
print(aps)

