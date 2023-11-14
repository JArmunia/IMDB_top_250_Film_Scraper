# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from fake_useragent import UserAgent
import requests
from random import randint
from urllib.parse import urlencode
from scrapy import signals
import random

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


class ImdbscraperSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)


class ImdbscraperDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)


class ScrapeOpsFakeUserAgentMiddleware:

    def __init__(self, settings):
        self.ua = UserAgent()

    def _get_random_user_agent(self):
        return self.ua.random

    def process_request(self, request, spider):
        random_user_agent = self._get_random_user_agent()
        request.headers["User-Agent"] = random_user_agent


class ScrapeOpsFakeBrowserHeaderAgentMiddleware:

    def __init__(self):
        self.ua = UserAgent()

    def generate_random_header(self):

        accept_types = [
            'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'application/json, text/javascript, */*; q=0.01',
            'application/xml,application/xhtml+xml,text/html;q=0.9,image/webp,*/*;q=0.8',
        ]

        accept_language = [
            # 'en-US,en;q=0.5',
            'en-GB,en;q=0.5',
            'es-ES,es;q=0.5',
            'fr-FR,fr;q=0.5'
        ]
        referers = [
            'https://www.google.com/',
            'https://www.bing.com/',
            'https://www.yahoo.com/',
            'https://duckduckgo.com/'
        ]

        dnt_options = ['1', '0']

        cache_control = [
            'no-cache',
            'max-age=0',
            'no-store'
        ]

        sec_fetch_user = ['?1', '?0']
        sec_fetch_mode = ['navigate', 'no-cors', 'cors', 'same-origin']
        sec_fetch_site = ['none', 'same-origin', 'same-site', 'cross-site']
        sec_ch_ua_platform = ['"Windows"', '"macOS"', '"Android"', '"iOS"']
        sec_ch_ua_mobile = ['?0', '?1']
        sec_ch_ua = [
            '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
            '"Google Chrome";v="90", "Chromium";v="90", "Microsoft Edge";v="90"'
        ]

        header = {
            'User-Agent': self.ua.random,
            'Accept': random.choice(accept_types),
            'Accept-Language': random.choice(accept_language),
            'Referer': random.choice(referers),
            'DNT': random.choice(dnt_options),
            'Cache-Control': random.choice(cache_control),
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': random.choice(sec_fetch_mode),
            'Sec-Fetch-Site': random.choice(sec_fetch_site),
            'Sec-Fetch-User': random.choice(sec_fetch_user),
            'Sec-Ch-Ua': random.choice(sec_ch_ua),
            'Sec-Ch-Ua-Mobile': random.choice(sec_ch_ua_mobile),
            'Sec-Ch-Ua-Platform': random.choice(sec_ch_ua_platform),
        }

        return header

    # Usar la función para obtener headers aleatorios

    def process_request(self, request, spider):
        random_header = self.generate_random_header()
        request.headers["User-Agent"] = random_header["User-Agent"]
        request.headers["Accept"] = random_header["Accept"]
        #request.headers["Accept-Language"] = random_header["Accept-Language"]
        request.headers["Referer"] = random_header["Referer"]
        request.headers["DNT"] = random_header["DNT"]
        request.headers["Cache-Control"] = random_header["Cache-Control"]
        request.headers["Sec-Fetch-Dest"] = random_header["Sec-Fetch-Dest"]
        request.headers["Sec-Fetch-Mode"] = random_header["Sec-Fetch-Mode"]
        request.headers["Sec-Fetch-Site"] = random_header["Sec-Fetch-Site"]
        request.headers["Sec-Fetch-User"] = random_header["Sec-Fetch-User"]
        request.headers["Sec-Ch-Ua"] = random_header["Sec-Ch-Ua"]
        request.headers["Sec-Ch-Ua-Mobile"] = random_header["Sec-Ch-Ua-Mobile"]
        request.headers["Sec-Ch-Ua-Platform"] = random_header["Sec-Ch-Ua-Platform"]

