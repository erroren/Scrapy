from scrapy import cmdline
name = 'Sun5'
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())