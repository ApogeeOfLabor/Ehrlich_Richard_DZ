def qwe(mail):
    # Немного схалявил) , но решил не списывать проверку email на валидность,
    # а когда пойму как правильно сам напишу.
    x = re.compile(r"(?:\w+[-.]*)+[^@]")
    y = x.findall(mail)
    user_data['username'] = y[0]
    user_data['domain'] = y[1]
    return user_data


if __name__ == '__main__':
    import re
    user_data = {'username': '', 'domain': ''}
    user_email = input('Enter email: ')
    if user_email.count('@') == 1:
        print(qwe(user_email))
