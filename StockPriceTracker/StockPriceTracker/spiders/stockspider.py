import scrapy


class StockspiderSpider(scrapy.Spider):
    name = "stockspider"
    allowed_domains = ["finance.yahoo.com"]
    start_urls = ["https://finance.yahoo.com/screener/unsaved/67bf0299-8f29-46c7-a355-03141239df5a?count=100&offset=0"]

    def parse(self, response):
        pass
