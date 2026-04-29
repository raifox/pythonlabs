def simple_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

class Car:
    wheels_count = 4

    def __init__(self, name="Невідомо", max_speed=0):
        self._name = name
        self.__max_speed = max_speed

    @property
    def max_speed(self):
        return self.__max_speed

    @max_speed.setter
    def max_speed(self, value):
        self.__max_speed = value

    @staticmethod
    def get_vehicle_type():
        return "Наземний транспорт"

    @simple_decorator
    def cost(self):
        return self.max_speed * 100

    def update_model(self):
        self.max_speed += 10

    def __str__(self):
        return f"Автомобіль: {self._name}, Швидкість: {self.max_speed} км/год"

    def __add__(self, other):
        return self.max_speed + other.max_speed

    def __sub__(self, other):
        return self.max_speed - other.max_speed

    def __mul__(self, value):
        return self.max_speed * value

    def __truediv__(self, value):
        return self.max_speed / value

    def __gt__(self, other):
        return self.max_speed > other.max_speed

    def __lt__(self, other):
        return self.max_speed < other.max_speed

    def __ge__(self, other):
        return self.max_speed >= other.max_speed

    def __le__(self, other):
        return self.max_speed <= other.max_speed

    def __eq__(self, other):
        return self.max_speed == other.max_speed

    def __ne__(self, other):
        return self.max_speed != other.max_speed


class ExecutiveCar(Car):
    def cost(self):
        return self.max_speed * 250

    def update_model(self):
        self.max_speed += 5


print("--- Завдання: Демонстрація роботи класів ---")

car1 = Car("Toyota", 200)
car2 = Car("Ford", 180)
exec_car = ExecutiveCar("Mercedes", 250)

print(car1)
print(exec_car)

print(Car.get_vehicle_type())
print(Car.wheels_count)

print(car1.cost())
print(exec_car.cost())

car1.update_model()
exec_car.update_model()
print(car1.max_speed)
print(exec_car.max_speed)

print(car1 + car2)
print(car1 - car2)
print(car1 * 2)
print(car1 / 2)

print(car1 > car2)
print(car1 == car2)