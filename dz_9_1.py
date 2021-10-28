from time import sleep
from itertools import cycle

class TrafficLight:
    __color = [('red', 7), ('yellow', 2), ('green', 12)]

    def running(self):
        for light in cycle(self.__color):
            print(f'\r{light[0]}', end='')
            sleep(light[1])

a = TrafficLight()
a.running()