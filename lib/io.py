def save2file(text, absolute_file_name):
    if not text:
        print '[ERROR]', 'no data to save', text
        return
    fh = open(absolute_file_name, 'w')
    fh.write(text)
    fh.close()
    print 'save 2 file ' + absolute_file_name + '(' + str(len(text)) + ')\n'

def readfile(absolute_file_name):
    fh = open(absolute_file_name, 'r')
    data = fh.readlines()
    return data
