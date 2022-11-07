import paho.mqtt.client as mqtt
import time
import base64

mqttBroker ="test.mosquitto.org"
client = mqtt.Client("ALPR_inside")
client.connect(mqttBroker) 
client.loop_start()
client.subscribe("ALPR")


def on_message(client, userdata, msg):
    print("received message: " ,str(msg.payload.decode("utf-8")))
    # msg = str(msg.payload.decode("utf-8"))
    # img = msg.encode('ascii')
    # final_msg = base64.b64decode(img)
    # open('received_image.jpg','wb').write(final_msg)


client.on_message = on_message

time.sleep(30)
#client.loop_forever()