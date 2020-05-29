class Car:
    name = None
    speed = None
    color = None
    is_police = None

    def __init__(self, name, speed, color, is_police):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return print('car go straight')

    def stop(self):
        return print('car stop')

    def turn(self, direction):
        return "The car turned to " + direction

    def show_speed(self):
        return self.speed

class TownCar(Car):
    def __init__(self, name: str, speed: int, color: str, is_police: bool ):
        self.name = name
        self.speed = speed
        self.color = color
        self. is_police = is_police

    def show_speed(self):
        if self.speed > 60:
            return 'Over speed! ' + str(self.speed)
        return str(self.speed)

class SporCar(Car):
    def __init__(self, name: str, speed: int, color: str, is_police: bool):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

class WorkCar(Car):
    def __init__(self, name: str, speed: int, color: str, is_police: bool):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def show_speed(self):
        if self.speed > 40:
            return 'Over speed! ' + str(self.speed)
        return str(self.speed)

class PoliceCar(Car):
    def __init__(self, name: str, speed: int, color: str, is_police: bool):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

towncar = TownCar()
sportcar = SporCar()
workcar = WorkCar()
policecar = PoliceCar()

print(towncar(name = 'Prius', speed = 60, color = ' Silver', is_police = False))


