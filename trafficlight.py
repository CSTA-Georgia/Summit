from hummingbird import Hummingbird
from time import sleep

bird = Hummingbird()

bird.set_single_led(1,255)
cars = []

while(len(cars) < 10):
    if(bird.get_light_sensor(1) < 30):
        cars.append(bird.get_light_sensor(1))
        sleep(.5)
        print(cars)

"""
Participants come up with your own sequence below
"""
#set green on and off
bird.set_single_led(1,0)
sleep(1.)
#set yellow on and off
bird.set_single_led(2,255)
sleep(3.0)
bird.set_single_led(2,0)

#set red on and off
bird.set_single_led(3,255)
sleep(5.0)
bird.set_single_led(3,0)

bird.close()


#stop our hkit
