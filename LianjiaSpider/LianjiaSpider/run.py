from scrapy import cmdline
name = 'temp'
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())