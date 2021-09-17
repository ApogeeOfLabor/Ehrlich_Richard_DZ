def currency_rates(url, name_valute):
    dom_data_valute = ET.fromstring(requests.get(url).text)
    current_date = requests.get(url).headers['Date']
    for country in dom_data_valute.findall('Valute'):
        code_valute = country.find('CharCode').text
        value_valute = country.find('Value').text
        if code_valute.lower() == name_valute.lower():
            return float('.'.join(value_valute.split(','))), current_date


if __name__ == '__main__':
    import requests
    import xml.etree.ElementTree as ET

    url = 'http://www.cbr.ru/scripts/XML_daily.asp'

    print(currency_rates(url, 'eur'), sep='\n')
