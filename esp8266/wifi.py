# WiFi

import network

# Create a station interface
sta = network.WLAN(network.STA_IF)

# Activate the interface
sta.active(True)

# Scan for access points and print the result
def scan_aps():
    aps = sta.scan()
    print(aps)


def connect_ap():
    if not wlan.isconnected():
        print("Connecting ...")
        wlan.connect("SSID", "PSK")

        while not wlan.isconnected():
            pass

    print("Connected!")
    print("Network config:", wlan.ifconfig())

scan_aps()
connect_ap()

