def make_files():
    for _ in range(25):
        name_and_weight = random.randint(1, 100000)
        if not os.path.exists(os.path.join(os.curdir, f"{name_and_weight}.txt")):
            with open(f"{name_and_weight}.txt", 'wb') as f:
                f.write(bytes(name_and_weight))


def getting_statistics(root, list_with_files):
    for file in list_with_files:
        if 0 < os.stat(os.path.join(root, file)).st_size < 101:
            stat_dict[100] += 1
        if 100 < os.stat(os.path.join(root, file)).st_size < 1001:
            stat_dict[1000] += 1
        if 1000 < os.stat(os.path.join(root, file)).st_size < 10001:
            stat_dict[10000] += 1
        if 10000 < os.stat(os.path.join(root, file)).st_size < 100001:
            stat_dict[100000] += 1


if __name__ == '__main__':
    import random
    import os

    stat_dict = {100: 0, 1000: 0, 10000: 0, 100000: 0}

    for path, dirs, files in os.walk(os.curdir):
        if len(files) != 0:
            getting_statistics(path, files)
    for item in stat_dict.items():
        print(f'{item[0]}: {item[1]}')
