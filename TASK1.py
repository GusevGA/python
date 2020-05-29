import time

class TrafficLight:
    _color = None

    def running(self):
        print('The light is on')
        self._color = 'red'
        print(f'Color light is: {self._color}')
        time.sleep(7)

        self._color = 'yellow'
        print(f'Color light is: {self._color}')
        time.sleep(2)

        self._color = 'green'
        print(f'Color light is: {self._color}')
        time.sleep(10)

traf_lig = TrafficLight()
print(traf_lig.running())