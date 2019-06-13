from scrapy import cmdline

name = "sunSpider"
cmd = "scrapy crawl {0}".format(name)
cmdline.execute(cmd.split())