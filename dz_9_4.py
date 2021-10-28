class Car:

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.color} {self.name} поехала')

    def stop(self):
        print(f'{self.color} {self.name} остановилась')

    def turn(self, direction):
        print(f'{self.color} {self.name} повернула {direction}')

    def show_speed(self):
        print(f'Скорость автомобиля: {self.speed}')

class TownCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        if self.speed > 60:
            print(f'Скорость автомобиля: {self.speed}, превышение скорости!')
        else:
            print(f'Скорость автомобиля: {self.speed}')

class WorkCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        if self.speed > 40:
            print(f'Скорость автомобиля: {self.speed}, превышение скорости!')
        else:
            print(f'Скорость автомобиля: {self.speed}')

class SportCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

class PoliceCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


c = Car(60, 'синий', 'Рено')
tc = TownCar(70, 'черный', 'Хендай')
wc = WorkCar(50, 'белая', 'Лада')
sc = SportCar(100, 'красная', 'Феррари')
pc = PoliceCar(80, 'голубой', 'Форд')

print(f'Машина: {c.name}, цвет: {c.color}, скорость: {c.speed}, машина полицейская: {c.is_police}')
print(f'Машина: {tc.name}, цвет: {tc.color}, скорость: {tc.speed}, машина полицейская: {tc.is_police}')
print(f'Машина: {wc.name}, цвет: {wc.color}, скорость: {wc.speed}, машина полицейская: {wc.is_police}')
print(f'Машина: {sc.name}, цвет: {sc.color}, скорость: {sc.speed}, машина полицейская: {sc.is_police}')
print(f'Машина: {pc.name}, цвет: {pc.color}, скорость: {pc.speed}, машина полицейская: {pc.is_police}')

c.go()
c.stop()
c.turn('налево')
c.show_speed()

tc.show_speed()
wc.show_speed()