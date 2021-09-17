def currency_rates(valute_code):
    valute_dict = {}
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text.split('</Valute>')
    current_date = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').headers['Date']
    date_obj = dateparser.parse(' '.join(current_date.split()[1:4]))
    end_ = str(date_obj).split()[0]
    for idx, value in enumerate(response):
        response[idx] = value.strip('<, >').split('><')
    for _, item in enumerate(response):
        for _, symbol in enumerate(item):
            if symbol.startswith('CharCode'):
                dict_key = symbol[symbol.find('>') + 1: symbol.find('<')]
                valute_dict[dict_key] = item
    for key, value in valute_dict.items():
        if key == valute_code.upper():
            for user_string in value:
                if user_string.startswith('Value'):
                    return float('.'.join(user_string[user_string.find('>') + 1: user_string.find('<')].split(','))), end_
                    # на момент написания кода , пока не понимаю как сделать по другому


if __name__ == '__main__':
    import requests
    import dateparser
    print(*currency_rates('usd'), sep='\n')
