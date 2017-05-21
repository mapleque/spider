import re
def regParse(reg, text):
    # aviod long string
    arr = []
    for line in text.split('\n'):
        olen = len(line)
        if olen > 10000:
            # sl = re.findall(r'.{100}', line)
            # sl.append(line[len(sl) * 100:])
            # line = '\n'.join(sl)
            line = line.replace('</p>', '</p>\n')
            print '[INFO]', 'line is too long divide to pieces', len(line) - olen
        arr.append(line)
    text = '\n'.join(arr)
    p = re.compile(reg)
    ret = []
    for m in p.finditer(text):
        ret.append(m.groups())
    return ret

# unit test
if __name__ == '__main__':
  ret = regParse(r'a(.?)', 'abacaabac')
  for groups in ret:
    print groups
