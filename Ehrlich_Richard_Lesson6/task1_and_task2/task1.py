def get_info(raw_response):
    for inner_string in raw_response.text.splitlines():
        ip = re.search(r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}', inner_string)
        req = re.search(r'[A-Z]{3,4}', inner_string)
        dom = re.search(r'/\w*/\w*_\d{1,2}', inner_string)
        yield ip.group(0), req.group(0), dom.group(0)


if __name__ == '__main__':
    import requests
    import re

    response = requests.get('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs')

    print(*get_info(response), sep='\n')
    # task1 done

    with open('modify_log_nginx.txt', 'w') as file:
        for inner_tuple in [*get_info(response)]:
            file.writelines(str(inner_tuple) + '\n')
