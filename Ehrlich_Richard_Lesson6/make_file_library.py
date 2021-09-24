def make_files(file_name, text=None):
    with open(file_name, 'w') as file:
        if text:
            file.write(text)


if __name__ == '__main__':
    make_files('users.csv', 'test text, again text')
