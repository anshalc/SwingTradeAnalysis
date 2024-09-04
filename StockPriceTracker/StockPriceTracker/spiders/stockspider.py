from urllib.error import HTTPError
import scrapy, sys
from StockPriceTracker.items import StockpricetrackerItem

class StockspiderSpider(scrapy.Spider):

    
    name = "stockspider"
    start_value = 0

    tickers = []

    def start_requests(self): # functiom to get the initial response from the website
        # base url of the site to scrape
        url_template = "https://finance.yahoo.com/screener/unsaved/67bf0299-8f29-46c7-a355-03141239df5a?c%20...%3A%20ount=100&count=100&offset={}"
        # first page of the url
        current_value = self.start_value
        # call to parse function for subsequent requests to pages
        yield scrapy.Request(url = url_template.format(current_value), callback = self.parse, errback=self.handle_error, meta = {'current_value': current_value})


    def parse(self, response):
        # getting all the tickers from our screener
        tickers = response.css('a[data-test="quoteLink"]::text').getall()
        # checking if the page contains tickers
        if tickers:
             item = StockpricetrackerItem()
             item['tickers'] = tickers
             yield item
        else:
            sys.exit(0)
        next_value = response.meta['current_value'] + 100
        next_url = f'https://finance.yahoo.com/screener/unsaved/67bf0299-8f29-46c7-a355-03141239df5a?c%20...%3A%20ount=100&count=100&offset={next_value}'
        yield scrapy.Request(url = next_url, callback = self.parse, errback=self.handle_error, meta={'current_value': next_value})
        

    def handle_error(self, failure):
        # Log the error or raise an exception
        self.log(f"Request failed with error: {failure.value}", level=scrapy.log.ERROR)

        # Optionally, raise an exception to stop the spider or take other actions
        if failure.check(HTTPError):
            response = failure.value.response
            self.log(f"HTTP Error: {response.status} for {response.url}", level=scrapy.log.ERROR)
        elif failure.check(LookupError):
            self.log("DNS Lookup Error", level=scrapy.log.ERROR)
        elif failure.check(TimeoutError, TCPTimedOutError):
            self.log("Timeout Error", level=scrapy.log.ERROR)
        else:
            self.log("General Error", level=scrapy.log.ERROR)

           
        
