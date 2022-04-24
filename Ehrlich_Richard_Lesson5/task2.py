def odd_numbers():
    total = list()
    for i in range(1, int(input()) + 1, 2):
        total.append(i)
    return total


if __name__ == '__main__':
    print(*odd_numbers(), sep='\n')

    # тот же результат можно сделать в одну строку из всего, что сверху
    print(*(item for item in range(1, int(input()) + 1, 2)), sep='\n')
