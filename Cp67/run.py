from scrapy import cmdline


cmdline.execute('scrapy crawl cp67 -o cp67.csv'.split())
# 存csv
# cmdline.execute('scrapy crawl cp67 -o cp67.csv'.split())