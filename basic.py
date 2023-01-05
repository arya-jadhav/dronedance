from djitellopy import tello
from time import sleep

drone = tello.Tello()
drone.connect()

print(drone.get_battery())

drone.takeoff()
drone.send_rc_control(20, 0, 0, 0)
sleep(2)
drone.send_rc_control(0, 20, 0, 0)
sleep(2)
drone.send_rc_control(0, 0, 0, 180)
sleep(2)
drone.flip_forward()
drone.land()