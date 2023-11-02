# WiFi

import network
import config as conf

# Scan for access points and print the result
def scan_aps():
    # Create a station interface
    sta = network.WLAN(network.STA_IF)

    # Activate the interface
    sta.active(True)

    aps = sta.scan()
    print(aps)

# Display information on station and ap interfaces
def check_interfaces():
    sta_if = network.WLAN(network.STA_IF)
    ap_if = network.WLAN(network.AP_IF)

    if sta_if.active():
        print("Station is active")
        print(sta_if.ifconfig())
    else:
        print("Station is not active")

    if ap_if.active():
        print("Hotspot is active")
        print(ap_if.ifconfig())
    else:
        print("Hotspot is not active")

# Connect to an access-point as a station
def connect_ap():
    # Create a station interface
    sta = network.WLAN(network.STA_IF)
    
    # Activate the interface
    sta.active(True)

    if not sta.isconnected():
        print("Connecting to " + conf.wifi_sta_essid + " ...")
        sta.connect(conf.wifi_sta_essid, conf.wifi_sta_psk)

        while not sta.isconnected():
            pass

    print()
    print("Wifi Connected!")
    print("Network config:", sta.ifconfig())

# Start as an access-point
def start_ap():
    ap = network.WLAN(network.AP_IF)
    ap.active(True)
    ap.config(essid=conf.wifi_ap_essid,password=conf.wifi_ap_psk)

# Disable the access-point interface
def disable_ap():
    ap = network.WLAN(network.AP_IF)
    ap.active(False)

