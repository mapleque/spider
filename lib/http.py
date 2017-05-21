import httplib,parser
def get(host, path = '/'):
    conn = httplib.HTTPConnection(host)
    conn.request('GET', path)
    res = conn.getresponse()
    if res.status != 200:
        print '[ERROR]', res.status, res.reason
        return ''
    data = res.read()
    conn.close()
    print '[INFO]', 'http get html from ' + host + path + ':size(' + str(len(data)) + ')\n'
    return data

def get_url(url):
    url_reg = '^(https?):\/\/([\w\-\.]+)+([\w\-\.,@?^=%&:\/~\+#]*[\w\-\@?^=%&\/~\+#])?$'
    parse_arr = parser.regParse(url_reg, url)
    if len(parse_arr) < 1:
        print '[ERROR]', 'illigal url', url
        return ''
    protal = parse_arr[0][0]
    host = parse_arr[0][1]
    path = parse_arr[0][2]
    if not path:
        path = '/'
    return get(host, path)

# unit test
if __name__ == '__main__':
    print get('www.mapleque.com')
    print get('www.mapleque.com', '/404')
