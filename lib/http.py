import httplib
def get(host, path = '/', data = {}):
  conn = httplib.HTTPConnection(host)
  conn.request('GET', path)
  res = conn.getresponse()
  if res.status != 200:
    print '[ERROR]', res.status, res.reason
    return ''
  data = res.read()
  conn.close()
  return data

# unit test
if __name__ == '__main__':
  print get('www.mapleque.com')
  print get('www.mapleque.com', '/404')
