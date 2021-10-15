# 4)
# Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
class Car:
    is_police = False

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        return print(f"{self.name} is moving forward")

    def stop(self):
        print("stop!")

    def turn(self, direction):
        return f'Turn to the {direction}!'

    def show_speed(self):
        return f'current vehicle speed: {self.speed}'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('over speed!')
        return f'current vehicle speed: {self.speed}'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('over speed!')
        return f'current vehicle speed: {self.speed}'


class PoliceCar(Car):
    is_police = True


a = TownCar(80, 'black', 'BMW')

a.go()
print(a.show_speed())
print(a.turn('left'))
print(a.turn('right'))
a.stop()

b = SportCar(140, 'red', 'Maserati')

b.go()
print(b.show_speed())
print(b.turn('left'))
print(b.turn('right'))
b.stop()

c = WorkCar(50, 'orange', 'volkswagen')

c.go()
print(c.show_speed())
print(c.turn('left'))
c.go()
print(c.turn('left'))
c.stop()

d = PoliceCar(60, 'orange', 'Ford')

d.go()
print(d.show_speed())
print(d.turn('left'))
d.go()
print(d.turn('left'))
d.stop()

print(a.is_police)
print(b.is_police)
print(c.is_police)
print(d.is_police)
