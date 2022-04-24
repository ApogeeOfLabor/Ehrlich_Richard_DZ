def currency_rates(name_valute):
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    dom_data_valute = ET.fromstring(response.text)
    date_obj = dateparser.parse(' '.join(response.headers['Date'].split()[1:4]))
    end_ = str(date_obj).split()[0]
    for inner_item in dom_data_valute.findall('Valute'):
        code_valute = inner_item.find('CharCode').text
        value_valute = inner_item.find('Value').text
        if code_valute.lower() == name_valute.lower():
            return float('.'.join(value_valute.split(','))), end_


if __name__ == '__main__':
    import requests
    import dateparser
    import xml.etree.ElementTree as ET
    print(*currency_rates('eur'), sep='\n')
