import paho.mqtt.client as mqtt
import time
import base64

def on_message(client, userdata, message):
    #print("received message: " ,str(message.payload.decode("utf-8")))
    msg= message.payload.decode("utf-8")
    encoded_msg = msg.encode("ascii")
    decoded_msg = base64.b64decode(encoded_msg)
    image_received= open('received_image.jpg','wb')
    image_received.write(decoded_msg)
    print("Image received")



def initializer(topic="ALPR"):
    print("Starting init")  
    mqttBroker ="test.mosquitto.org"
    client = mqtt.Client("ALPR_inside")
    client.connect(mqttBroker) 
    client.loop_start()
    client.subscribe("ALPR")

    client.on_message=on_message 
    time.sleep(300)
    client.loop_stop()

if __name__ == '__main__':

    initializer()
    print("Done")