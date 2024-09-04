# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json


class StockpricetrackerPipeline:
    def open_spider(self, spider):
        self.stocks = []

    def process_item(self, item, spider):
        for ticker in item['tickers']:
            self.stocks.append({
                "ticker": ticker,
                "url": f"https://finance.yahoo.com/quote/{ticker}/"
            })
        return item
    
    def close_spider(self, spider):
        # write all the tickers to a JSON file
        with open('Stocks.json', 'w') as file:
            json.dump(self.stocks, file, indent=4)

