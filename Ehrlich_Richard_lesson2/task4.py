employee_data = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
print(id(employee_data), employee_data)
for item, name in zip(employee_data, [name[-1].capitalize() for name in [s.split() for s in employee_data]]):
    _tmp = item.split()
    _tmp[-1] = name
    employee_data[employee_data.index(item)] = ' '.join(_tmp)
    print(f'Привет {name}!')
print(id(employee_data), employee_data)
