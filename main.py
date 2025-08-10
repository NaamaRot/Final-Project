import gpiozero
import os
from time import sleep
import us_mode
import camera_mode

Button = gpiozero.Button

shutdown = Button(10)
cam = Button(13)
mode = Button(6)
us = Button(26)

right_motor = gpiozero.OutputDevice(12)
left_motor = gpiozero.OutputDevice(5)

try:
    while True:
        if mode.is_pressed:
            if us.is_pressed:
                sub_mode = "in"             
            else:
                sub_mode = "out"
            min_dist, side = us_mode.get_min_distance(sub_mode)
            timers = us_mode.get_timers(min_dist, sub_mode)
            if side == "left":
                us_mode.vibrate_side(timers, left_motor)
            elif side == "right":
                us_mode.vibrate_side(timers, right_motor)
            else:
                us_mode.vibrate(timers, right_motor, left_motor)
                
        else:
            if cam.is_pressed:
                print("capture")
                camera_mode.on_press(right_motor, left_motor)
        sleep(0.5)
        if shutdown.is_pressed:
            print("shutdown")
            os.system("sudo shutdown -h now")
        
except KeyboardInterrupt:
    print("\nProgram stopped")

