# Crawler config
start_urls = ['http://localhost:8080/archives.html']
download_delay = 2
custom_settings = {
  'SCHEDULER_ORDER' : 'BFO',
  'REQUESTS_QUEUE_SIZE' : 1,
  'SPIDER_MIDDLEWARES' : {
      'custom_depth_mw.DomainDepthMiddleware': 900,
      'scrapy.spidermiddlewares.depth.DepthMiddleware': None
  }
}
# Middleware config
DOMAIN_DEPTHS = {'localhost': 3, 'evrard.me': 2}
DEPTH_LIMIT = 1