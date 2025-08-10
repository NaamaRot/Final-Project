from gpiozero import DistanceSensor, OutputDevice
from time import sleep

# sen = sensor
# dist = distance
# l = left, m = middle, r = right
sen_l = DistanceSensor(echo=18, trigger=17)
sen_m = DistanceSensor(echo=23, trigger=27)
sen_r = DistanceSensor(echo=24, trigger=22)

in_over_100 = (0, 1)
in_100 = (0.2, 0.8)
in_80 = (0.4, 0.6)
in_80 = (0.6, 0.4)
in_40 = (0.8, 0.2)
in_20 = (1, 0)

out_over_300 = (0, 1)
out_300 = (0.1, 0.9)
out_250 = (0.3, 0.7)
out_200 = (0.5, 0.5)
out_150 = (0.7, 0.3)
out_100 = (0.9, 0.1)
out_50 = (1, 0)

def get_min_distance(sub_mode):
    if sub_mode == "out":
        sen_l.max_distance = 3
        sen_l.threshold_distance = 0.5
        sen_m.max_distance = 3
        sen_m.threshold_distance = 0.5
        sen_r.max_distance = 3
        sen_r.threshold_distance = 0.5
        
        dist_l = sen_l.distance
        dist_m = sen_m.distance
        dist_r = sen_r.distance
        
        if dist_m == 3:
            if dist_l > dist_r:
                return (dist_r * 100, "right")
            else:
                return (dist_l * 100, "left")
        else:
            return (dist_m, "both")
    else:
        sen_l.max_distance = 1
        sen_l.threshold_distance = 0.2
        sen_r.max_distance = 1
        sen_r.threshold_distance = 0.2
        
        dist_l = sen_l.distance
        dist_r = sen_r.distance
        
        if dist_l > dist_r:
            return (dist_r * 100, "right")
        else:
            return (dist_l * 100, "left")
    
def vibrate_side(timers, motor):
    if timers[0] == 0:
        sleep(1)
    else:
        motor.on()
        sleep(timers[0])
        motor.off()
        sleep(timers[1])
        
def vibrate(timers, motor1, motor2):
    if timers[0] == 0:
        sleep(1)
    else:
        motor1.on()
        motor2.on()
        sleep(timers[0])
        motor1.off()
        motor2.off()
        sleep(timers[1])
        
def get_timers(dist, sub_mode):
    if sub_mode == "out":
        if dist >= 300:
            return (0, 1)
        elif dist > 250:
            return (0.1, 0.9)
        elif dist > 200:
            return(0.3, 0.7)
        elif dist > 150:
            return (0.5, 0.5)
        elif dist > 100:
            return (0.7, 0.3)
        elif dist > 50:
            return (0.9, 0.1)
        else:
            return (1, 0)
    else:
        if dist >= 100:
            return (0, 1)
        elif dist > 80:
            return (0.2, 0.8)
        elif dist > 60:
            return (0.4, 0.6)
        elif dist > 40:
            return (0.6, 0.4)
        elif dist > 20:
            return (0.8, 0.2)
        else:
            return (1, 0)


