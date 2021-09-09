weather_report = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(id(weather_report), *weather_report)
number_index_list = list()
for index, value in enumerate(weather_report):
    if value.isdigit():
        weather_report[index] = f'{format(int(value)):>02}'
        number_index_list.append(index)
    elif value[0] == '-' or value[0] == '+':
        signed_number = list(value)
        signed_number[-1] = ('{:02d}'.format(int(signed_number[-1])) if len(signed_number) == 2 else signed_number[1:])
        weather_report[index] = '{}'.format(''.join(signed_number))
        number_index_list.append(index)

print(id(weather_report), weather_report)
