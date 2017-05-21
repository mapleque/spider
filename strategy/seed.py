def deal(groups, outpath, spider):
    text = ''
    for group in groups:
        append = group[0][1:]
        name = group[1]
        url = 'http://www.stats.gov.cn/tjsj/tjbz/xzqhdm' + append
        #reg = r'<p.*?class="MsoNormal".*?(\d{6}).*?<span style=.*?>(.*?)<.*?<\/p>'
        reg = r'<p.*?class="MsoNormal".*?(\d{6})(.*?)<\/p>'
        spider(url, reg, 'areacode', outpath+'/'+name+'.data')
        text += url + '\n'
    file_handler = open(outpath+'/seed.dat', 'w')
    file_handler.write(text)
    print 'create file(' + str(len(text)) + '): ' + outpath +'/seed'
    file_handler.close()
