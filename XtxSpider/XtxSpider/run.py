from scrapy import cmdline
name = 'xtx'
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())