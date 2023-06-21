def val_checker(type_checking):
    def decor(function):
        def wrapper(*args: int):
            try:
                filter(type_checking, args)
                # map(type_checking, args)
                result = function(*args)
                return result
            except TypeError:
                raise TypeError("Invalid data type")

        return wrapper

    return decor


@val_checker(lambda value: value > 0)
def calc_cube(*args: int or tuple) -> list:
    return [num ** 3 for num in args]


if __name__ == '__main__':
    print(*calc_cube(5, 9))
