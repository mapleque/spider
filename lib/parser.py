import re
def regParse(reg, text):
  p = re.compile(reg)
  ret = []
  for m in p.finditer(text):
    ret.append(m.groups())
  return ret

# unit test
if __name__ == '__main__':
  ret = regParse(r'a(.?)', 'abacaabac')
  for groups in ret:
    print groups[0]
