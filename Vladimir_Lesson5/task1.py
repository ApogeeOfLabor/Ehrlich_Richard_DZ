def odd_numbers(): yield from range(1, int(input()) + 1, 2)


if __name__ == '__main__':
    print(*odd_numbers(), sep='\n')
