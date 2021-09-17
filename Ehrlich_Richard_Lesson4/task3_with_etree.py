def currency_rates(name_valute):
    dom_data_valute = ET.fromstring(requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text)
    current_date = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').headers['Date']
    for country in dom_data_valute.findall('Valute'):
        code_valute = country.find('CharCode').text
        value_valute = country.find('Value').text
        if code_valute.lower() == name_valute.lower():
            return float('.'.join(value_valute.split(','))), current_date


if __name__ == '__main__':
    import requests
    import xml.etree.ElementTree as ET

    print(currency_rates('eur'), sep='\n')
