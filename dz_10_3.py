class Cell:
     def __init__(self, cell):
          self.cell = cell

     def __add__(self, other):
          return Cell(self.cell + other.cell)

     def __sub__(self, other):
          return Cell(self.cell - other.cell if self.cell - other.cell >=0 \
                           else print('Операция неверная! Разность больше нуля'))

     def __mul__(self, other):
          return Cell(self.cell * other.cell)

     def __floordiv__(self, other):
          return Cell(self.cell // other.cell)

     def __truediv__(self, other):
          return Cell(self.cell // other.cell)

     def make_order(self, cell_in_row):
          for _ in range(self.cell // cell_in_row):
               print('*' * cell_in_row)
          print('*' * (self.cell % cell_in_row))

a = Cell(11)
b = Cell(7)

print((a + b).cell)
print((a - b).cell)
print((a * b).cell)
print((a // b).cell)
print((a / b).cell)

a.make_order(5)
b.make_order(6)