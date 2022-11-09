import paho.mqtt.client as mqtt 
from random import randrange, uniform
import time
import base64

mqttBroker ="test.mosquitto.org" 

client = mqtt.Client("ALPR_inside")
client.connect(mqttBroker) 

with open("car.jpg", "rb") as img_file:
    my_string = base64.b64encode(img_file.read())
    
message = my_string.decode('ascii')

#base64_bytes = base64.b64encode(message)
#base64_message =base64_bytes.decode('ascii')
client.publish("ALPR", message)
print("Just published to topic")

time.sleep(1) 

 

""" def run_publisher():

    mqttBroker ="test.mosquitto.org" 

    client = mqtt.Client("ALPR_inside")
    client.connect(mqttBroker)

    with open("car.jpg", "rb") as img_file:
        my_string = base64.b64encode(img_file.read())
        
    message = my_string.decode('ascii')

    client.publish("ALPR", message)
    print("Just published to topic")

    time.sleep(1) 
 """


 