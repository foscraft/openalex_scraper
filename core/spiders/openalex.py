import scrapy


class OpenalexSpider(scrapy.Spider):
    name = "openalex"
    allowed_domains = ["absch.cbd.int"]
    start_urls = ["http://absch.cbd.int/"]

    def parse(self, response):
        pass
