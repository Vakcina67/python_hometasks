class Stationery:
    title = 'Канцелярсякая принадлежность'

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print('Пишем ручкой')

class Pencil(Stationery):
    def draw(self):
        print('Рисуем карандашом')

class Handle(Stationery):
    def draw(self):
        print('Чертим маркером')

a, b, c, d = Stationery(), Pen(), Pencil(), Handle()
a.draw()
b.draw()
c.draw()
d.draw()
