
#gpio zero allows RPi to control the GPIOs
from gpiozero import LED, Robot, MotionSensor
#allows program to wait and measure time
from time import sleep
#define the GPIOs for nerf gun
relay4 = LED(26)
relay3 = LED(19)
switch = LED(13)
nerfGun = LED(6)
#turn the motors on
switch.on()
nerfGun.on()
#start Bluetooth

#motion sensor GPIO
pir = MotionSensor(25)

def fire():
    #allows nerf gun to warm up so bullets go faster
    nerfGun.off()
    time.sleep(0.5)
    switch.off()
    #push bullet forward
    relay4.on()
    relay3.on()
    #wait for it to go all the way
    sleep(0.5)
    #pull pen back
    relay3.off()
    relay4.off()
    sleep(0.5)
    nerfGun.on()
    switch.on()
while True:
    #waits until sensor detects motion in front of it
    pir.wait_for_motion()
    fire()
    time.sleep(0.3)
