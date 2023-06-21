def get_info(raw_response):
    for inner_string in raw_response.iter_lines():
        data = re.match(r"^([\w.|:]+[^\s_]).+\"([A-Z]+)\s([/\w]+).+$", inner_string.decode()).groups()
        yield data[0], data[1], data[2]


if __name__ == '__main__':
    import requests
    import re

    response = requests.get('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs')

    with open('modify_log_nginx.txt', 'w') as file:
        for inner_tuple in get_info(response):
            file.write(f'{inner_tuple}\n')
