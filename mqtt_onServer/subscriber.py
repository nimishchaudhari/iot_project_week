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
    print("message received")


""" 
    message = str(message.payload.decode("utf-8"))
    decoded_msg = base64.b64decode(message)
    image_received= open('received_image.jpg','wb').write(decoded_msg)
    print("image received")

    image_received.close()
 """

mqttBroker ="test.mosquitto.org"
client = mqtt.Client("Smartphone")
client.connect(mqttBroker) 
client.loop_start()
client.subscribe("ALPR")


""" def on_message(client, userdata, message):
    print("received message: " ,str(message.payload.decode("utf-8"))) """
       
client.on_message=on_message 
time.sleep(30)
client.loop_stop()
#client.loop_forever()


""" def initializer():
    print("Starting init")  
    mqttBroker ="test.mosquitto.org"
    client = mqtt.Client("ALPR_inside")
    client.connect(mqttBroker) 
    # client.loop_start()
    client.subscribe(topic)

    client.on_message=on_message 
    print("On message command done")
    time.sleep(30)
    client.loop_stop()
    if os.path.isfile(img):
    
        # print(LPR.get_license_number())               # LP Number 


        # Put this info in MongoDB
    
if __name__ == '__main__':

    initializer()
    print("Done") """