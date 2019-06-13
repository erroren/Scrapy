from scrapy import cmdline

name = 'Mytest'
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())