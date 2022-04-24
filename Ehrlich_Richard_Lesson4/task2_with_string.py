def currency_rates(url, valute_code):
    valute_dict = {}
    response = requests.get(url).text.split('</Valute>')
    for idx, value in enumerate(response):
        response[idx] = value.strip('<, >').split('><')
    for _, item in enumerate(response):
        for _, symbol in enumerate(item):
            if symbol.startswith('CharCode'):
                dict_key = symbol[symbol.find('>') + 1: symbol.find('<')]
                valute_dict[dict_key] = item
    for key, value in valute_dict.items():
        if key == valute_code:
            for user_string in value:
                if user_string.startswith('Value'):
                    return '.'.join(user_string[user_string.find('>') + 1: user_string.find('<')].split(','))


if __name__ == '__main__':
    import requests
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    print(currency_rates(url, 'USD'))
