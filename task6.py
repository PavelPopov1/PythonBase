import time
import itertools as it
import random as rd

# 1


class TrafficLight:
    def __init__(self):
        self.__current_color = 'Off'
        self.__color_list = ['Red', 'Yellow', 'Green']
        print('Светофор создан')

    def run(self, time_sec):
        print(f'Светофор включен на {time_sec} c')
        time_start = time.time()
        for i, num in enumerate(it.cycle(self.__color_list)):
            self.__current_color = num
            print(self.__current_color)
            if not i % 3 or i % 3 == 2:
                time.sleep(7)
            else:
                time.sleep(2)
            if time.time() - time_start >= time_sec:
                print('Светофор выключен')
                break


Light = TrafficLight()
Light.run(28)


# 2


class Road:
    def __init__(self, length, width, thickness, weig_unit):
        self._length, self._width, self._thickness, self._weig_unit = length, width, thickness, weig_unit
        self._weight = None

    def set_weight(self):
        try:
            self._weight = int(self._length) * int(self._width) * int(self._thickness) * int(self._weig_unit)
        except ValueError as e:
            print('Класс инициализрован неверно')

    def get_weight(self):
        return self._weight


asp_road = Road(1000, 50, 5, 25)
asp_road.set_weight()
print(asp_road.get_weight())


# 3


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name, self.surname, self.position = name, surname, position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return {'first_name': self.name, 'last_name': self.surname}

    def get_total_income(self):
        return sum(self._income.values())


bob_worker = Position('Bob', 'Livingston', 'Data-engineer', 300000, 50000)
print(bob_worker.get_full_name())
print(bob_worker.get_total_income())
print(bob_worker.position)

print()
kate_worker = Position('Kate', 'Livingston', 'Data-science', 200000, 30000)
print(kate_worker.get_full_name())
print(kate_worker.get_total_income())
print(kate_worker.position)


# 4

class Car:
    def __init__(self, color, name, is_police):
        self.color = color
        self.name = name
        self.is_police = is_police
        self._speed = 0

    def go(self):
        self._speed = rd.randint(30, 100)
        print('Машина поехала')

    def stop(self):
        self._speed = 0
        print('Машина остановилась')

    def turn(self, direction):
        if not self._speed:
            raise Exception('Невозможно, машина остановлена')
        else:
            self._speed -= rd.randint(10, 20)
            if not self._speed:
                self._speed = 0
            print(f'Машина повернула на {direction}')

    def show_speed(self):
        return self._speed


class TownCar(Car):
    def __init__(self, color, name):
        is_police = False
        super().__init__(color, name, is_police)
        print('this town car')

    def show_speed(self):
        if self._speed > 60:
            print(f'do not break! Speed: {self._speed}')
        return self._speed

    def go(self):
        self._speed = rd.randint(30, 90)
        print('Машина поехала')


class SportCar(Car):
    def __init__(self, color, name):
        is_police = False
        super().__init__(color, name, is_police)
        print('this sport car')

    def go(self):
        self._speed = rd.randint(50, 300)
        print('Машина поехала')


class WorkCar(Car):
    def __init__(self, color, name):
        is_police = False
        super().__init__(color, name, is_police)
        print('this work car')

    def show_speed(self):
        if self._speed > 40:
            print(f'do not break! Speed: {self._speed}')
        return self._speed

    def go(self):
        self._speed = rd.randint(20, 60)
        print('Машина поехала')


class PoliceCar(Car):
    def __init__(self, color, name):
        is_police = True
        super().__init__(color, name, is_police)
        print('this police car')

    def go(self):
        self._speed = rd.randint(40, 200)
        print('Машина поехала')


car_und = Car('Red', 'Lada', False)
car_und.go()
print(car_und.show_speed())

print()
car_t = TownCar('Green', 'Opel')
car_t.go()
print(car_t.show_speed())
car_t.turn('left')
print(car_t.show_speed())
car_t.stop()

print()
car_w = WorkCar('Yellow', 'Niva')
car_w.go()
print(car_w.show_speed())
car_w.turn('left')
print(car_w.show_speed())
print(car_w.color)
car_w.stop()
print(car_w.show_speed())

print()
car_sport = SportCar('Red', 'Ferrari')
car_sport.go()
print(car_sport.show_speed())
car_sport.turn('right')
print(car_sport.show_speed())
car_sport.stop()
print(car_sport.show_speed())

print()
car_police = PoliceCar('Black', 'Lamborghini')
car_police.go()
print(car_police.show_speed())
car_police.turn('right')
print(car_police.show_speed())
car_police.stop()
print(car_police.show_speed())
print(car_police.is_police)


# 5


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки при помощи ручки')


class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки при помощи карандаша')


class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки при помощи маркера')


pen_obj = Pen('Pen')
pencil_obj = Pencil('Pencil')
handle_obj = Handle('Handle')
pen_obj.draw()
pencil_obj.draw()
handle_obj.draw()








