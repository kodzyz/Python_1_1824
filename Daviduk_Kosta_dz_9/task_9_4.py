# task_9_4.py
# Реализуйте базовый класс Car:
# атрибуты: speed, color, name, is_police(булево)
# методы: go, stop, turn(direction) + show_speed
#дочерние классы: TownCar, SportCar, WorkCar, PoliceCar
#переопределить метод show_speed(TownCar, WorkCar):
#При скорости свыше 60 (TownCar) и 40 (WorkCar) выводиться сообщение о превышении скорости.

class Car:
    def __init__(self, name, color, speed=0, is_police: bool = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        if self.speed == 0:
            return print(f'{False} "go": "{self.color} {self.name}" stand:\n{self.show_speed()}')
        else:
            return print(f'{True} "go": yes! "{self.color} {self.name}" are driving\n{self.show_speed()} ')

    def stop(self):
        if self.speed == 0:
            return print(f'{True} "stop": yes! "{self.color} {self.name}" are standing\n{self.show_speed()}')
        else:
            return print(f'{False} "stop": "{self.color} {self.name}" are driving\n{self.show_speed()}')

    def turn(self, direction):
        self.direction = direction
        if self.direction in ['right', 'left', 'forward', 'back']:
            return print(f'"{self.color} {self.name}" direction is "{self.direction}"')
        else:
            raise Exception('Error!\nwrong direction\nchoose from:\n "right" or "left" or "forward" or "back"')

    def show_speed(self):
        return f'"{self.color} {self.name}" speed = {self.speed}'

f = Car('Lexus', 'Gray', 0)
f.stop()
f.turn('left')
# True "stop": yes! "Gray Lexus" are standing
# "Gray Lexus" speed = 0
# "Gray Lexus" direction is "left"


class PoliceCar(Car):
    def police(self):
        if self.is_police is True:
            return print(f'"{self.color} {self.name}" is "{self.__class__.__name__}"')
        else:
            return print(f'"{self.color} {self.name}" is not "{self.__class__.__name__}"')

g = PoliceCar('Audi', 'White', 40, False)
g.police()
g.go()
g.turn('forward')
# "White Audi" is not "PoliceCar"
# True "go": yes! "White Audi" are driving
# "White Audi" speed = 40
# "White Audi" direction is "forward"
print(g.is_police)
#False


class SportCar(Car):
    def __init__(self, name, color, speed=0, is_police: bool = False, is_sport_car: bool = True):
        super().__init__(name, color, speed, is_police)
        self.is_sport_car = is_sport_car

    def sport(self):
        if self.is_sport_car is True:
            return print(f'"{self.color} {self.name}" is "{self.__class__.__name__}"')
        else:
            return print(f'"{self.color} {self.name}" is not "{self.__class__.__name__}"')

s = SportCar('Jaguar', 'Red', 250, False, True)
s.sport()
#"Red Jaguar" is "SportCar"
print(s.show_speed())
# "Red Jaguar" speed = 250
s.go()
# True "go": yes! "Red Jaguar" are driving
# "Red Jaguar" speed = 250

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return print(f'Attention: "{self.color} {self.__class__.__name__} {self.name}" OverSpeed!')


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return print(f'Attention: "{self.color} {self.__class__.__name__} {self.name}" OverSpeed!')

t = TownCar('Tramcar', 'Sapphirine', 65)
w = WorkCar('БелАЗ', 'White', 45)

t.show_speed()
#Attention: "Sapphirine TownCar Tramcar" OverSpeed!
t.turn('left')
#"Sapphirine Tramcar" direction is "left"
w.show_speed()
#Attention: "White WorkCar БелАЗ" OverSpeed!
print(s.show_speed())
#"Red Jaguar" speed = 250