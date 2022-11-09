import paho.mqtt.client as mqtt #import the client1
import time
import paho.mqtt.subscribe as subscribe

def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    # print("message topic=",message.topic)
    # print("message qos=",message.qos)
    # print("message retain flag=",message.retain)
    pass
########################################


broker_address="test.mosquitto.org"

# print("creating new instance")
client = mqtt.Client("XEXE112") #create new instance

client.on_message=on_message #attach function to callback
# print("connecting to broker")
client.connect(broker_address) #connect to broker

client.loop_start() #start the loop
# print("Subscribing to topic","ALPR")
client.subscribe("ALPR")
time.sleep(400) # wait
client.loop_stop() #stop the loop