class Road:
    _length = 500
    _width = 8

    def __init__(self, length, width, mass, thickness):
        self._length = length
        self._width = width
        self._mass = mass / 1000
        self._thickness = thickness


    def asphalt_mass(self):
        return self._length * self._width * self._mass * self._thickness

a = Road(10, 177, 23, 14)
print(a.asphalt_mass())


