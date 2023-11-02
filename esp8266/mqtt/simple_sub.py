import time
from umqtt.simple import MQTTClient
import mqtt.config as conf


# Received messages from subscriptions will be delivered to this callback
def sub_cb(topic, msg):
    print((topic, msg))

# Connect to a broker and subscribe for messages on the configured topic
def main(server=conf.server):
    print("Connecting to broker ...")
    print("MQTT Server: " + conf.server)
    print("Subscribing to: " + str(conf.topic))

    c = MQTTClient(conf.client_id, server, conf.port, conf.username, conf.password)
    c.set_callback(sub_cb)
    c.connect()
    c.subscribe(conf.topic)

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
