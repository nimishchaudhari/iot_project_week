import paho.mqtt.client as mqtt 
from random import randrange, uniform
import time
import base64

mqttBroker ="test.mosquitto.org" 

client = mqtt.Client("Temperature_Inside")
client.connect(mqttBroker) 

""" while True:
    randNumber = uniform(20.0, 21.0)
    client.publish("TEMPERATURE", randNumber)
    print("Just published " + str(randNumber) + " to topic TEMPERATURE")
    time.sleep(1) """

while True:
    with open("car.jpg","rb") as image:
            img = image.read()
        
    message =img
    base64_bytes = base64.b64encode(message)
    base64_message =base64_bytes.decode('ascii')
    client.publish("TEMPERATURE", base64_message)
    print("Just published to topic TEMPERATURE")
    time.sleep(1) 

    
