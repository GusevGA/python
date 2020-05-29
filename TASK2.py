class Road:
    _length = None
    _width = None
    _weight = 25
    _thikness = 0.05

    def __init__(self, length, width ):
        self._length = length
        self._width = width

    def project(self):
        return self._length*self._width*self._weight*self._thikness

road = Road(length = 5000, width = 20)
print(f'You need {road.project()} tonns of asphalt')