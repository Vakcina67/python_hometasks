from abc import ABC, abstractmethod

class MyAbstractClass_1(ABC):
     @abstractmethod
     def calc_suit(self):
          pass

class MyAbstractClass_2(ABC):
     @abstractmethod
     def calc_coat(self):
          pass

class Suit(MyAbstractClass_1):
     def __init__(self, H):
          self.H = H

     @property
     def calc_suit(self):
          return self.H * 2 + 0.3

class Coat(MyAbstractClass_2):
     def __init__(self, V):
          self.V = V

     @property
     def calc_coat(self):
          return self.V / 6.5 + 0.5

suit_size = Suit(160)
print(suit_size.calc_suit)

coat_size = Coat(48)
print(coat_size.calc_coat)

sum_cloth = suit_size.calc_suit + coat_size.calc_coat
print(sum_cloth)


