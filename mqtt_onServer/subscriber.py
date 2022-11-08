import paho.mqtt.client as mqtt
import time
import base64, LPR, os
img = 'mqtt_onServer/received_image.jpg'

def on_message(client, userdata, message):
    #print("received message: " ,str(message.payload.decode("utf-8")))
    msg= message.payload.decode("utf-8")
    encoded_msg = msg.encode("ascii")
    decoded_msg = base64.b64decode(encoded_msg)
    # if os.path.isfile(img):
    image_received= open(img,'wb')
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
    if os.path.isfile(img):
    
        print(LPR.get_license_number())               # LP Number 


        # Put this info in MongoDB
    client.loop_forever()

if __name__ == '__main__':

    initializer()
    print("Done")