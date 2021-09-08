temp_info = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(id(temp_info), *temp_info)
for num in temp_info:
    if num.isdigit():
        temp_info[temp_info.index(num)] = ('"{}"'.format(num) if len(num) == 2 else '"{0:02d}"'.format(int(num)))
    elif num[0] == '-' or num[0] == '+':
        signed_number = list(num)
        signed_number[-1] = ('{:02d}'.format(int(signed_number[-1])) if len(signed_number) == 2 else signed_number[1:])
        temp_info[temp_info.index(num)] = '"{}"'.format(''.join(signed_number))
print(id(temp_info), *temp_info)
