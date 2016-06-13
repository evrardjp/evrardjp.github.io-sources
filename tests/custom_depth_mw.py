import logging
from scrapy.http import Request
import config

class DomainDepthMiddleware(object):
    def __init__(self, domain_depths, default_depth):
        self.domain_depths = config.DOMAIN_DEPTHS
        self.default_depth = config.DEPTH_LIMIT
        logging.debug("Domain Depths are set to %s" % self.domain_depths)

    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings
        domain_depths = settings.getdict('DOMAIN_DEPTHS', default={})
        default_depth = settings.getint('DEPTH_LIMIT', 1)

        return cls(domain_depths, default_depth)

    def process_spider_output(self, response, result, spider):
        def _filter(request):
            if isinstance(request, Request):
                # get max depth per domain
                for specific_domain in self.domain_depths:
                    if specific_domain in request.url:
                        maxdepth = self.domain_depths.get(specific_domain)
                    else:
                        maxdepth = self.default_depth

                depth = response.meta.get('depth', 0) + 1
                request.meta['depth'] = depth

                if maxdepth and depth > maxdepth:
                    logging.debug("Ignoring link (depth > %d): %s "
                        % (maxdepth, request.url))
                    return False
                else:
                    logging.info('Processing link %s' % request.url)
            return True

        return (r for r in result or () if _filter(r))