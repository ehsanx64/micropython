# Application entrypoint (should be loaded in boot.py)

print()

def info(title, content=""):
    if content == "":
        print(title + " ...")
    else:
        print(title + ": " + content)

info("Loading config")
import config as conf

def main():
    info("Loading app")

    # Enable wifi connection if configured
    if conf.app_wifi_station:
        import wifi
        wifi.connect_ap()

if conf.app_autostart == True:
    info("Autostart triggered")
    main()
else:
    info("Autostart bypassed")

# Additional code as application


