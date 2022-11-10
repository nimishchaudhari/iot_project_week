from LPR import get_license_number as gln
from Camera import take_photo           # "mqtt_onRPI/photo.jpg"
from time import sleep
import paho.mqtt.publish as publish


# Take photo first

print("Taking photo in 3 seconds")
sleep(3)
#img = take_photo("mqtt_onRPI/photo.jpg")
#LP_number = gln("mqtt_onRPI/photo.jpg")
img = take_photo("photo.jpg")
LP_number =gln("photo.jpg")



publish.single('ALPR', LP_number, hostname='test.mosquitto.org')
