# WiFi

import network

# Scan for access points and print the result
def scan_aps():
    # Create a station interface
    sta = network.WLAN(network.STA_IF)
    
    # Activate the interface
    sta.active(True)
    
    aps = sta.scan()
    print(aps)

def connect_ap():
    # Create a station interface
    sta = network.WLAN(network.STA_IF)
    
    # Activate the interface
    sta.active(True)

    if not wlan.isconnected():
        print("Connecting ...")
        wlan.connect("SSID", "PSK")

        while not wlan.isconnected():
            pass

    print("Connected!")
    print("Network config:", wlan.ifconfig())

def start_ap():
    ap = network.WLAN(network.AP_IF)
    ap.active(True)
    ap.config(essid="ESP1-AP",password="asdfasdf")

#scan_aps()
#connect_ap()
start_ap()
