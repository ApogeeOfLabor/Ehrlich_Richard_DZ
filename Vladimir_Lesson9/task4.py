class Car:
    name = ''
    color = ''
    is_police = ''
    speed = 0

    def __init__(self, name: str, color: str, is_police: bool, speed:int):
        self.name = name
        self.color = color
        self.is_police = is_police
        self.speed = speed

    def go(self):
        print('GO!')

    def stop(self):
        print('STOP!')

    def turn(self, derection):
        print(f"I'm turning {derection}")

    def show_speed(self):
        print(f'Speed: {self.speed}')


class TownCar(Car):
    def __init__(self, name: str, color: str, is_police: bool, speed: int):
        super().__init__(name, color, is_police, speed)
        if self.speed > 60:
            print(f'Your speed is {self.speed}, you have to slow down now!')

    def show_speed(self):
        print(f'Your speed: {self.speed}')


class WorkCar(Car):
    def __init__(self, name: str, color: str, is_police: bool, speed: int):
        super().__init__(name, color, is_police, speed)
        if self.speed > 40:
            print(f'Your speed is {self.speed}, you have to slow down now!')

    def show_speed(self):
        print(f'Your speed: {self.speed}')


class SportCar(Car):
    def __init__(self, name: str, color: str, is_police: bool, speed: int):
        super().__init__(name, color, is_police, speed)


class PoliceCar(Car):
    def __init__(self, name: str, color: str, is_police: bool, speed: int):
        super().__init__(name, color, is_police, speed)


if __name__ == '__main__':
    bmw = TownCar('X7', 'Black', False, 170)
