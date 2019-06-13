from scrapy import cmdline

name='Txtx'
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())