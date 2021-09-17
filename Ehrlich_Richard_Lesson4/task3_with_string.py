def currency_rates(url, valute_code):
    valute_dict = {}
    response = requests.get(url).text.split('</Valute>')
    current_date = requests.get(url).headers['Date']
    for index, value in enumerate(response):
        response[index] = value.strip('<, >').split('><')
    for _, item in enumerate(response):
        for _, str in enumerate(item):
            if str.startswith('CharCode'):
                dict_key = str[str.find('>') + 1 : str.find('<')]
                valute_dict[dict_key] = item
    for key, value in valute_dict.items():
        if key == valute_code.upper():
            for user_string in value:
                if user_string.startswith('Value'):
                    return float('.'.join(user_string[user_string.find('>') + 1 : user_string.find('<')].split(','))), current_date
                    # на момент написания кода , пока не понимаю как сделать по другому


if __name__ == '__main__':
    import requests
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    print(currency_rates(url, 'usd'))
