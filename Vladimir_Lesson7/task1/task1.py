import os

import yaml
from yaml.loader import SafeLoader

print(os.getcwd())
with open('config.yaml', 'rb') as file:
    reader = yaml.load(file, Loader=SafeLoader)
    for root, folders in reader.items():
        for folder in folders:
            try:
                os.makedirs(os.path.join(root, folder))
            except FileExistsError as error:
                print('Папка уже существует\n', error)
