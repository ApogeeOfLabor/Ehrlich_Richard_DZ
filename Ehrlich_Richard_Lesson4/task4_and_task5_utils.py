def currency_rates(argv):
    programs, *args = argv
    dom_data_valute = ET.fromstring(requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text)
    current_date = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').headers['Date']
    for inner_item in dom_data_valute.findall('Valute'):
        code_valute = inner_item.find('CharCode').text
        value_valute = inner_item.find('Value').text
        for input_code_valute in args:
            if code_valute.lower() == input_code_valute.lower():
                print(float('.'.join(value_valute.split(','))), current_date)


if __name__ == '__main__':
    import sys
    import requests
    import xml.etree.ElementTree as ET

    exit(currency_rates(sys.argv))
