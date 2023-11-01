import time
from umqtt.simple import MQTTClient

mqserver="127.0.0.1"
mqport="1883"
username="user"
password="pass"
topic=b"mqttpy/simple"

# Received messages from subscriptions will be delivered to this callback
def sub_cb(topic, msg):
    print((topic, msg))

def main(server=mqserver):
    print("Connecting to broker ...")
    c = MQTTClient("umqtt_client", server, mqport, username, password)
    c.set_callback(sub_cb)
    c.connect()
    c.subscribe(topic)
    while True:
        if True:
            # Blocking wait for message
            c.wait_msg()
        else:
            # Non-blocking wait for message
            c.check_msg()
            # Then need to sleep to avoid 100% CPU usage (in a real
            # app other useful actions would be performed instead)
            time.sleep(1)

    c.disconnect()


if __name__ == "__main__":
    main()
