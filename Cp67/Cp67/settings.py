# -*- coding: utf-8 -*-

# Scrapy settings for Cp67 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

# 需要修改的变量
# 模块地址
MODULE_URL = 'https://www.cq67.com/jingyan/'
# 爬取的页数
PAGE_NUM = 1000
# 分类名称
CATEGORY = '养生经验'

# 数据库配置
MYSQL_HOST = '47.93.185.202'
MYSQL_USER = 'health'
MYSQL_PWD = 'f47e992be1f7fea5'
MYSQL_DB = 'dedecms_health'

# 日志相关变量
LOG_LECEL = "INFO"
LOG_FILE = 'spoder.log'

# 存json和csv格式
FEED_EXPORT_ENCODING = 'utf-8'

# # 分布式配置
# # 重新指定调度器: 启用Redis调度存储请求队列
# SCHEDULER = "scrapy_redis.scheduler.Scheduler"
#
# # 重新指定去重机制: 确保所有的爬虫通过Redis去重
# DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
#
# # 不清除Redis队列: 暂停/恢复/断点续爬
# SCHEDULER_PERSIST = False
#
# # 优先级队列 （默认）
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.PriorityQueue'
# # # 可选用的其它队列
# # # 先进先出队列
# # SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.FifoQueue'
# # # 后进先出队列
# # SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.LifoQueue'
#
# # 指定连接到redis时使用的端口和地址
# REDIS_HOST = '39.106.1.89'
# REDIS_PORT = 6379


BOT_NAME = 'Cp67'

SPIDER_MODULES = ['Cp67.spiders']
NEWSPIDER_MODULE = 'Cp67.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'Cp67 (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'Cp67.middlewares.Cp67SpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'Cp67.middlewares.Cp67DownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'Cp67.pipelines.Cp67Pipeline': 300,
    # 存入redis
    # 'scrapy_redis.pipelines.RedisPipeline': 200,
    'Cp67.pipelines.Cp67MysqlPipeline': 100,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
