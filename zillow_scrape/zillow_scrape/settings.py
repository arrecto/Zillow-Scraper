# Scrapy settings for zillow_scrape project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

# BOT_NAME = "zillow_scrape"

SPIDER_MODULES = ["zillow_scrape.spiders"]
NEWSPIDER_MODULE = "zillow_scrape.spiders"


# Crawl responpsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    "Content-Type": "application/json",
    "Cookie":"zguid=24|%248699d4d9-5919-48ee-a9cf-8cac3d61d3f6; zjs_anonymous_id=%228699d4d9-5919-48ee-a9cf-8cac3d61d3f6%22; zjs_user_id=null; zg_anonymous_id=%22406a49b5-2b56-47d2-99f1-94c46efe522f%22; _ga=GA1.2.1357832159.1726057091; _pxvid=e96d9230-7037-11ef-8a28-0938446dfffb; _gcl_au=1.1.162681960.1726057093; _fbp=fb.1.1726057092780.757571963332032239; _pin_unauth=dWlkPU9UUmxaVE0yTVRFdFpEaGlNaTAwWW1FM0xXSTNNamt0Wm1SbE1qRXpOR0k0WWpVNA; _cs_c=0; _scid=WAbw-ERPtmxcXpwo8Bljv2wbvHEyghFP; _tt_enable_cookie=1; _ttp=90_daUowPXa9yEE5OwPI4Hsnb2o; optimizelyEndUserId=oeu1727871303839r0.7551473646814533; zgcus_aeut=AEUUT_f4bdbaff-80b7-11ef-a806-52eb50b6d09e; zgcus_aeuut=AEUUT_f4bdbaff-80b7-11ef-a806-52eb50b6d09e; _ga_4XV6G3SPH9=GS1.2.1727871305.1.0.1727871305.60.0.0; _cs_id=bc1eeee3-2e7f-a458-e900-d4be3a86cabb.1726057093.2.1727871305.1727871305.1.1760221093626.1; zgsession=1|c95cb4c1-f9ae-4553-b025-16bfde9346c2; _gid=GA1.2.202153744.1729341802; pxcts=b9f16aa1-8e17-11ef-8508-b7b6bf8e2bfe; JSESSIONID=0CEAABFEBC7F420CF74AA0FE0C91E0A6; _rdt_uuid=1726057093199.4bd580f2-fc79-4036-aa24-807b1ba67cd7; tfpsi=bb1855fd-f870-459f-acca-bbc4fd32d513; _scid_r=aIbw-ERPtmxcXpwo8Bljv2wbvHEyghFPuwFw9Q; _clck=1iallt7%7C2%7Cfq5%7C0%7C1715; _ScCbts=%5B%22157%3Bchrome.2%3A2%3A5%22%5D; DoubleClickSession=true; _sctr=1%7C1729267200000; _dd_s=rum=0&expire=1729343175019; AWSALB=AhETny3eBRPtBxQh3ErHCnnD1gbuDb0pncGLHgtHrYwQTXqWRT9rbdkZT/OmNrCgYQpKXciKGaq2m4f2f8RIrfOAEXwOh6+qrubQv3C67AeMxsuAdr9nqzDoVKeJ; AWSALBCORS=AhETny3eBRPtBxQh3ErHCnnD1gbuDb0pncGLHgtHrYwQTXqWRT9rbdkZT/OmNrCgYQpKXciKGaq2m4f2f8RIrfOAEXwOh6+qrubQv3C67AeMxsuAdr9nqzDoVKeJ; _px3=62991d87239fd0d559e44d875f312011b44e628ebac32b3a8ba252c5f3a08221:R6qu5vmhPGzXZF9RPyIfwF391jirhEXmjUI79CEjc82qzU1QXt+4fMUy8nKvd7B/DUB0V2lFQh7JhV34LSK+9Q==:1000:R6pmmmiJ6vVWPG8kh6rIDUCQkjCRwE2RPh2rak89rLLmdyiwf5ifGhQmMv669t5qE5S4SpJ5nrCKoXzjuuW0Ys0buRPCwEMSkG+1FUdAyWU2ULDQVM79sXxoZcD13wzwMmUR3CrgjxaCuPZzGj5TfFgHfD/9U9XXiaEZaIJ3K4byxBRTgyOawEO0yH0Sn6lD38o7SGEmljF7SobwXNujZHC384GyqjWmZt5Vu6YcPVE=; search=6|1731934279853%7Crect%3D22.180681422549895%2C-159.28324936224365%2C22.13481453819099%2C-159.33380363775635%26rid%3D98845%26disp%3Dmap%26mdm%3Dauto%26p%3D1%26z%3D1%26listPriceActive%3D1%26fs%3D1%26fr%3D0%26mmm%3D0%26rs%3D0%26ah%3D0%26singlestory%3D0%26housing-connector%3D0%26parking-spots%3Dnull-%26abo%3D0%26garage%3D0%26pool%3D0%26ac%3D0%26waterfront%3D0%26finished%3D0%26unfinished%3D0%26cityview%3D0%26mountainview%3D0%26parkview%3D0%26waterview%3D0%26hoadata%3D1%26zillow-owned%3D0%263dhome%3D0%26featuredMultiFamilyBuilding%3D0%26student-housing%3D0%26income-restricted-housing%3D0%26military-housing%3D0%26disabled-housing%3D0%26senior-housing%3D0%26commuteMode%3Ddriving%26commuteTimeOfDay%3Dnow%09%0998845%09%7B%22isList%22%3Atrue%2C%22isMap%22%3Atrue%7D%09%09%09%09%09; _uetsid=bd405f108e1711efadb3cf7508d994c8; _uetvid=ea869e10703711ef82994d8f547cd99a; __gads=ID=962643280cae9390:T=1727871443:RT=1729342280:S=ALNI_MZTI2zOjHeSboMP28-qVyriAFVbyA; __gpi=UID=00000f2edc874bbe:T=1727871443:RT=1729342280:S=ALNI_MaXX_E9jjasMMOsZ4rYgiIXwQNGBg; __eoi=ID=228d146d7078b03f:T=1727871443:RT=1729342280:S=AA-AfjaIrJJMTSh6PofocqEeuR9B; _clsk=rspxm3%7C1729342281422%7C3%7C1%7Cp.clarity.ms%2Fcollect",
    "Origin":"https://www.zillow.com",
    "Referer":"https://www.zillow.com/homes/96703_rb/"}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "zillow_scrape.middlewares.ZillowScrapeSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "zillow_scrape.middlewares.ZillowScrapeDownloaderMiddleware": 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    "zillow_scrape.pipelines.ZillowScrapePipeline": 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
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
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
