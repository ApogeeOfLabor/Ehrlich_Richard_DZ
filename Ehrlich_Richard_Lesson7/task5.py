def getting_statistics(root, list_with_files):
    for file in list_with_files:
        if 0 <= os.stat(os.path.join(root, file)).st_size < 101:
            add_values(100, file)
        if 100 < os.stat(os.path.join(root, file)).st_size < 1001:
            add_values(1000, file)
        if 1000 < os.stat(os.path.join(root, file)).st_size < 10001:
            add_values(10000, file)
        if 10000 < os.stat(os.path.join(root, file)).st_size < 100001:
            add_values(100000, file)


def add_values(key, file):
    if len(stat_dict[key][1]) == 0:
        stat_dict[key] = 1, [file.split('.')[-1]]
    else:
        value = stat_dict[key]
        if file.split('.')[1] in value[1]:
            stat_dict[key] = value[0] + 1, value[1]
        else:
            value[1].append(file.split('.')[1])
            stat_dict[key] = value[0] + 1, value[1]


if __name__ == '__main__':
    import os

    stat_dict = {100: (0, []), 1000: (0, []), 10000: (0, []), 100000: (0, [])}

    for path, dirs, files in os.walk(os.curdir):
        if len(files) > 0:
            getting_statistics(path, files)
    for item in stat_dict.items():
        print(f'{item[0]}: {item[1]}')
