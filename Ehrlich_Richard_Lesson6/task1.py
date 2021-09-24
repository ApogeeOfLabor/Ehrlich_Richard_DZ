import requests
url = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
response = requests.get(url).text.split('\n')
xlist = []
for _, string in enumerate(response):
    for string_item in string.split():
        if string_item.strip('", -'):
            xlist.append(string_item.strip('", -'))
    ip = xlist[0] if string.split() else ''
    wois_request = xlist[3] if string.split() else ''
    domain_pointer = xlist[4] if string.split() else ''
    print((ip, wois_request, domain_pointer))
    xlist.clear()
