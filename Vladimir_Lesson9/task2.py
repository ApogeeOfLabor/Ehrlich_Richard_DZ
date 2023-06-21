class Road:

    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width

    def get_all_asphalt_weight(self, asphalt_weight, thickness):
        return f"{self.lenght * self.width * asphalt_weight * thickness // 1000}т"


if __name__ == '__main__':
    x = Road(20, 5000)
    print(x.get_all_asphalt_weight(25, 5))
