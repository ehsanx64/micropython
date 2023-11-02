import network
import webrepl_setup
import webrepl
import config as conf

def start_ap():
    ap = network.WLAN(network.AP_IF)
    ap.active(True)
    ap.config(essid=conf.wifi_ap_essid,password=conf.wifi_ap_psk)


start_ap()
webrepl.start()

# Use https://github.com/micropython/webrepl to connect to the webrepl shell
# Follow the instructions afterwards to setup autostart and login password