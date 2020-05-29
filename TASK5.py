class Stationery:
    title: str

    def draw(self):
        return 'Запуск отрисовки'

class Pen(Stationery):
    title = 'Ручкой'

    def draw(self):
        return self.title

class Pencil(Stationery):
    title = 'Карандашом'

    def draw(self):
        return self.title

class Handle(Stationery):
    title = 'Маркером'

    def draw(self):
        return self.title

stationery = Stationery()
pen = Pen()
pencil = Pencil()
handle = Handle()
print(stationery.draw())
print(pen.draw())
print(pencil.draw())
print(handle.draw())