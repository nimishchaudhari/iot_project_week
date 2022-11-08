#import the necessary packages
from gpiozero import Button, MotionSensor
from picamera import PiCamera
from time import sleep
from signal import pause

#create objects that refer to a button,
#a motion sensor and the PiCamera
# button = Button(2)
# pir = MotionSensor(4)
camera = PiCamera()

#start the camera
camera.rotation = 180
# camera.start_preview()


#stop the camera when the pushbutton is pressed
# def stop_camera():
#     camera.stop_preview()
    #exit the program
    # exit()

#take photo when motion is detected

def take_photo():
    print("Clicking in 3 secs")
    sleep(3)
    camera.capture('/home/pi/iot_project_week/mqtt_onRPI/car.jpg')
    print('A photo has been taken')
    camera.close()

#assign a function that runs when the button is pressed
# button.when_pressed = stop_camera
# #assign a function that runs when motion is detected
# pir.when_motion = take_photo

# pause()