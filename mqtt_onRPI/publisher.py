import paho.mqtt.client as mqtt 
from random import randrange, uniform
import time
import base64


def run_publisher():

    mqttBroker ="test.mosquitto.org" 

    client = mqtt.Client("ALPR_inside")
    client.connect(mqttBroker)

    with open("/home/pi/iot_project_week/mqtt_onRPI/car.jpg", "rb") as img_file:
        my_string = base64.b64encode(img_file.read())
        
    message = my_string.decode('ascii')

    client.publish("ALPR", message)
    print("Just published to topic")

    time.sleep(1) 

