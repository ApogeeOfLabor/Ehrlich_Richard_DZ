employee_data = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
print(id(employee_data), employee_data)
for item in employee_data:
    employee_data[employee_data.index(item)] = f"{' '.join(item.split()[:-1])} {item.split()[-1]}"
    print(f'Привет {item.split()[-1]}!')
print(id(employee_data), employee_data)
