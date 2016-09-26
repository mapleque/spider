import lib.http, lib.parser
def spider(seed, reg, indexStrategy = '', out_path = '/tmp'):
  text = lib.http.get(seed)
  groups = lib.parser.regParse(reg, text)
  if indexStrategy:
    index = __import__('index.' + indexStrategy)
    strategy = getattr(index, indexStrategy)
    strategy.deal(groups, out_path)

# unit test
if __name__ == '__main__':
  spider('www.mapleque.com', r'<a.*?href="(.*?)".*?</a>', 'default')

