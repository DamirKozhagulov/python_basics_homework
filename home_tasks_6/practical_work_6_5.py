# 5)
# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки'


class Pen(Stationery):
    def draw(self):
        return f'Штрих ручкой'


class Pencil(Stationery):
    def draw(self):
        return f'Штрих карандашом'


class Handle(Stationery):
    def draw(self):
        return f'Штрих маркером'


a = Pen(print("Работа ручкой"))
print(a.draw())

b = Pencil(print("Работа карандашом"))
print(b.draw())

c = Handle(print("Работа маркером"))
print(c.draw())
