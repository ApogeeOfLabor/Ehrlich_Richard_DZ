import random

# Получаем случайный список цен (я понимаю, что в задании написано создать в ручную), но так интереснее :)
random_number_list = [float('{0:.02f}'.format(random.randint(1, 16) * num)) for num in [random.random() for _ in range(15)]]
print(id(random_number_list), random_number_list)


def get_price_template(price_list):
    print_list = []
    for item in [str(n).split('.') for n in price_list]:
        print_list.append('{0} руб {1:02d} коп,'.format(item[0], int(item[1])) if len(item[1]) == 1 else '{0} руб {1} коп,'.format(item[0], item[1]))
    print(*print_list, end='\n\n')


# Step A
get_price_template(random_number_list)

# Step B
# Сортировка списка без изменения объекта
random_number_list.sort()
print(id(random_number_list), random_number_list, 'Step B')
get_price_template(random_number_list)

# Step C
# Новый список с теми же ценами в обратном порядке
another_random_number_list = random_number_list[::-1]
print(id(another_random_number_list), another_random_number_list, 'Step C')
get_price_template(another_random_number_list)

# Step D
print(id(random_number_list), random_number_list[-5:], 'Step D')
get_price_template(random_number_list[-5:])
