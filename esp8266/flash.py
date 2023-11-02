# ESP8266 flash functions

import os

# Print filesystem usage statistics
def usage_info():
    stats = os.statvfs('/')
    total = stats[0] * stats[2]
    free = stats[1] * stats[3]
    used = total - free
    print("Filesystem Usage")
    print("Total: " + str(total) + " bytes")
    print("Used: " + str(used) + " bytes")
    print("Free: " + str(free) + " bytes")

