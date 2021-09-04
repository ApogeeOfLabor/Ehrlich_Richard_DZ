number_tuple = ('процент', 'процента', 'процентов')
num_list = ['2', '3', '4']
for percent in range(1, 1001):
    if percent == 1 or (len(str(percent)) > 1 and str(percent)[-1] == str(1) and str(percent)[-2] != str(1)):
        print(f'{percent} {number_tuple[0]}')
    elif str(percent) in num_list or (len(str(percent)) > 1 and str(percent)[-2] != str(1) and (str(percent)[-1] in num_list)):
        print(f'{percent} {number_tuple[1]}')
    else:
        print(f'{percent} {number_tuple[2]}')
# Временами у меня мозг крайне не поворотливый. Так что пока более оптимизированное решение не пришло в голову.
