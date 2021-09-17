def currency_rates(url, valute_code):
    valute_dict = {}
    response = requests.get(url).text.split('</Valute>')
    for index, value in enumerate(response):
        response[index] = value.strip('<, >').split('><')
    for _, item in enumerate(response):
        for _, str in enumerate(item):
            if str.startswith('CharCode'):
                dict_key = str[str.find('>') + 1 : str.find('<')]
                valute_dict[dict_key] = item
    for key, value in valute_dict.items():
        if key == valute_code:
            for user_string in value:
                if user_string.startswith('Value'):
                    return '.'.join(user_string[user_string.find('>') + 1 : user_string.find('<')].split(','))


if __name__ == '__main__':
    import requests
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    print(currency_rates(url, 'USD'))
