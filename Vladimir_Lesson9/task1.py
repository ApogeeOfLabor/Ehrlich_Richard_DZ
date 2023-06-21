import time


class TrafficLight:
    __color = ''

    def __init__(self):
        pass

    def running(self):
        while True:
            for color, sec in zip(['Красный', 'Желтый', 'Зелёный'], [7, 2, 7]):
                self.__color = color
                print(self.__color)
                time.sleep(sec)


if __name__ == '__main__':
    x = TrafficLight()
    x.running()
