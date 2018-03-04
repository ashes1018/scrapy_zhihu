# -*- coding: utf-8 -*-

# Scrapy settings for zhangjiawei_followers project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html


BOT_NAME = 'zhangjiawei_followers'

SPIDER_MODULES = ['zhangjiawei_followers.spiders']
NEWSPIDER_MODULE = 'zhangjiawei_followers.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'zhangjiawei_followers (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
ITEM_PIPELINES = {
    'zhangjiawei_followers.pipelines.ZhangjiaweiFollowersPipeline': 800,
}


# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 0.25
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
  # 'Accept': 'application/json, text/plain, */*',
  # 'Accept-Language': 'en-GB,en;q=0.8,zh-CN;q=0.6,zh;q=0.4',
  'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
  'authorization':'Bearer Mi4xNjloVUFBQUFBQUFBVUFMZFZvMVVEQmNBQUFCaEFsVk5RQjdXV1FDWHU4THBDOGVIeXFkUC1rWGFqNmQ5dVJ1TE1R|1504612672|6342c5b374b3db8ae3e2c8fa02541939f5518f14'
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'zhangjiawei_followers.middlewares.ZhangjiaweiFollowersSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware':None,
    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': None,
    'zhangjiawei_followers.middlewares.ZhangjiaweiFollowersSpiderMiddleware': 125,
    'scrapy.contrib.downloadermiddleware.retry.RetryMiddleware': 500,
    'scrapy.contrib.downloadermiddleware.redirect.RedirectMiddleware': 600,
    # 'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware':None
}
RETRY_ENABLED = True
RETRY_TIMES = 1

#    'zhangjiawei_followers.middlewares.MyCustomDownloaderMiddleware': 543,
#}
#
# ip = [
# {"ipaddr":"175.22.184.29:80"},
# {"ipaddr":"113.128.90.239:48888"},
# {"ipaddr":"42.224.100.117:8118"},
# {"ipaddr":"60.221.49.46:8118"},
# {"ipaddr":"113.128.90.215:48888"}
# ]
#
# IPPOOL = ip


#Mysql数据库的配置信息
MYSQL_HOST = '127.0.0.1'
MYSQL_DBNAME = 'yulan'         #数据库名字，请修改
MYSQL_USER = 'root'             #数据库账号，请修改
MYSQL_PASSWD = 'ashes'         #数据库密码，请修改
MYSQL_PORT = 3306



# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'zhangjiawei_followers.pipelines.ZhangjiaweiFollowersPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

