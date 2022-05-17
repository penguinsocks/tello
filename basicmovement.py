from djitellopy import tello
from time import sleep

me = tello.Tello()
print(me.get_battery())
me.takeoff()
me.move_up(140)
sleep(.5)
# drone will move forward 600cm
me.move_forward(200)
me.move_forward(200)
me.move_forward(200)
sleep(.5)
# drone will turn and then move 300cm
me.rotate_counter_clockwise(90)
sleep(.5)
me.move_forward(300)
sleep(.5)
# drone will rotate and move froward 600cm
me.rotate_counter_clockwise(90)
sleep(.5)
me.move_forward(200)
me.move_forward(200)
me.move_forward(200)
sleep(.5)
# drone will turn and move forward 300cm
me.rotate_counter_clockwise(90)
sleep(.5)
me.move_forward(300)
sleep(.5)
# drone will turn and land
me.rotate_counter_clockwise(90)
sleep(.5)
me.land()
