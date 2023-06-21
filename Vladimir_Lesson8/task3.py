def type_logger(function):
    # @wraps  # or we can use function -> wraps with export from functools
    def wrapper(*args, **kwargs):
        print(*[f'{num}: {type(num)}' for num in args if args])
        res = function(*args, **kwargs)
        return function.__name__, *[f'{num}: {type(num)}' for num in res if res]
    wrapper.__name__ = function.__name__
    wrapper.__doc__ = function.__doc__
    return wrapper


@type_logger
def calc_cube(*args, **kwargs):
    """ Some note's """
    if kwargs: res = (item ** 3 for item in kwargs.values())
    return (num ** 3 for num in args) if args else res


if __name__ == '__main__':
    print(*calc_cube(num=5, c=3))
    print(calc_cube.__name__)
    print(help(calc_cube))
