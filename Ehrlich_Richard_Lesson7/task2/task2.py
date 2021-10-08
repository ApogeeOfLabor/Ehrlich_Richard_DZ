import os
import yaml


def make_from_list(entered_root, items_list):
    for item in items_list:
        if isinstance(item, dict):
            make_from_dict(entered_root, item)
        elif isinstance(item, list):
            make_from_list(entered_root, item)
        elif isinstance(item, str):
            make_from_string(entered_root, item)


def make_from_dict(entered_root, entered_reader):
    for inner_root, values in entered_reader.items():
        if not os.path.exists(os.path.join(entered_root, inner_root)):
            os.makedirs(os.path.join(entered_root, inner_root), exist_ok=False)
        new_root = os.path.join(entered_root, inner_root)
        if isinstance(values, list):
            make_from_list(new_root, values)
        if isinstance(values, dict):
            make_from_dict(new_root, values)
        if isinstance(values, str):
            make_from_string(new_root, values)


def make_from_string(entered_root, entered_string):
    if '.' in entered_string:
        if not os.path.exists(os.path.join(entered_root, entered_string)):
            with open(os.path.join(entered_root, entered_string), 'w') as f:
                f.write('')
    else:
        if not os.path.exists(os.path.join(entered_root, entered_string)):
            os.makedirs(os.path.join(entered_root, entered_string), exist_ok=False)


def main(config_file):
    with open(config_file, 'r') as file:
        reader = yaml.safe_load(file)
        root = os.curdir
        if isinstance(reader, dict):
            make_from_dict(root, reader)
        if isinstance(reader, list):
            make_from_list(root, reader)
        elif isinstance(reader, str):
            make_from_string(root, reader)


if __name__ == '__main__':
    main('config.yaml')
