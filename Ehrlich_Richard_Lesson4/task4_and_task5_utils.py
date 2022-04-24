def currency_rates(argv):
    programs, *args = argv
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    dom_data_valute = ET.fromstring(response.text)
    date_obj = dateparser.parse(' '.join(response.headers['Date'].split()[1:4]))
    end_ = str(date_obj).split()[0]
    for inner_item in dom_data_valute.findall('Valute'):
        code_valute = inner_item.find('CharCode').text
        value_valute = inner_item.find('Value').text
        for input_code_valute in args:
            if code_valute.lower() == input_code_valute.lower():
                print(float('.'.join(value_valute.split(','))), end_)


if __name__ == '__main__':
    import sys
    import dateparser
    import requests
    import xml.etree.ElementTree as ET

    exit(currency_rates(sys.argv))
