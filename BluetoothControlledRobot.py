#import bluedot to connect RPi to Blutooth so it can be controlled
from bluedot import BlueDot
#gpio zero allows RPi to control the GPIOs
from gpiozero import LED, Robot
#used for Bluetooth
from signal import pause
#allows program to wait and measure time
from time import sleep
#define the GPIOs for nerf gun
relay4 = LED(26)
relay3 = LED(19)
switch = LED(13)
nerfGun = LED(6)
#turn the motors on
switch.off()
nerfGun.off()
#start Bluetooth
bd = BlueDot()
#robot GPIOs
robot = Robot(left = (9, 10), right = (7, 8))

def fire():
    #allows nerf gun to warm up so bullets go faster
    nerfGun.on()
    time.sleep(0.5)
    switch.on()
    #push bullet forward
    relay4.on()
    relay3.on()
    #wait for it to go all the way
    sleep(0.5)
    #pull pen back
    relay3.off()
    relay4.off()
    sleep(0.5)
    nerfGun.off()
    switch.off()

#movement
def move(pos):
    if pos.top:
        robot.left()
    elif pos.bottom:
        robot.right()
    elif pos.left:
        robot.forward()
    elif pos.right:
        robot.backward()
    elif pos.middle:
        fire()

#lack of movement
def stop():
    robot.stop()

bd.when_pressed = move
bd.when_moved = move
bd.when_released = stop

pause()
