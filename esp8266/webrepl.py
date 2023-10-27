import network
import webrepl_setup
import webrepl

def start_ap():
    ap = network.WLAN(network.AP_IF)
    ap.active(True)
    ap.config(essid="ESP1-AP",password="asdfasdf")


start_ap()
webrepl.start()

# Use https://github.com/micropython/webrepl to connect to the webrepl shell
# Follow the instructions afterwards to setup autostart and login password