def copy_templates(inner_root, entered_path):
    for dir_obj in os.scandir(entered_path):
        if isinstance(dir_obj, os.DirEntry):
            if '.' in dir_obj.name:
                with open(os.path.join(inner_root, dir_obj.name), 'w') as f:
                    f.write('')
            else:
                if not os.path.exists(os.path.join(inner_root, dir_obj.name)):
                    os.mkdir(os.path.join(inner_root, dir_obj.name))
                if os.stat(os.path.join(inner_root, dir_obj.name)).st_size:
                    copy_templates(os.path.join(inner_root, dir_obj.name), os.path.join(entered_path, dir_obj.name))


if __name__ == '__main__':
    import os

    root = os.path.join(os.curdir, 'my_project')
    for index, (path, dirs, files) in enumerate(os.walk('../task2/')):
        if path.split('/')[-1] == 'templates':
            new_root = f'{root}/{path.split("/")[-1]}/'
            if not os.path.exists(new_root):
                os.mkdir(new_root)
            if os.stat(path).st_size:
                copy_templates(new_root, path)
