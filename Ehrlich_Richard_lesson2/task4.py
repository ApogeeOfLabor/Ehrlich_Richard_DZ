employee_data = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
print(id(employee_data), employee_data)
for item, name in zip(employee_data, [s[s.rindex(' ') + 1:].capitalize() for s in employee_data]):
    employee_data[employee_data.index(item)] = f"{item[:item.rindex(' ')]} {name}"
    print(f'Привет {name}!')
print(id(employee_data), employee_data)
# думаю такой алгоритм дешевле
