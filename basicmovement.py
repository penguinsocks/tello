
from djitellopy import tello
from time import sleep

me = tello.Tello()
me.connnect()
print(me.get_battery())
