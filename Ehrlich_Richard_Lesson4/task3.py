def currency_rates():
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    return response.text


if __name__ == '__main__':
    import requests
    print(currency_rates(), sep='\n')
