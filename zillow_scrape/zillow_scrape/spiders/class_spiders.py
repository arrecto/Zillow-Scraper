from bs4 import BeautifulSoup
import scrapy
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
import pandas as pd
import json
from scrapy.utils.reactor import install_reactor

# install_reactor("twisted.internet.asyncioreactor.AsyncioSelectorReactor")
# property_runner = CrawlerRunner(get_project_settings())


#obtain the listing information (mls id, link)
class ListingSpider(scrapy.Spider):
    name = 'listing_spider'

    # def __init__(self, zipcode: int):
    #     self.zipcode = zipcode

    #do not scrape if maxpage 
    def start_requests(self):
        request_url = 'https://www.zillow.com/async-create-search-page-state'
        # payload = {"searchQueryState":{"pagination":{},"isMapVisible":False,"mapBounds":{"west":-159.33380363775635,"east":-159.28324936224365,"south":22.13481453819099,"north":22.180681422549895},"usersSearchTerm":self.zipcode,"filterState":{"sortSelection":{"value":"globalrelevanceex"},"isAllHomes":{"value":True}},"isListVisible":True,"mapZoom":14},"wants":{"cat1":["listResults"],"cat2":["total"]},"requestId":3,"isDebugRequest":False}
        payload = {"searchQueryState":{"isMapVisible":False,"mapBounds":{"west":-160.50209597928747,"east":-158.84316043241247,"south":20.95800324619129,"north":22.430477493443448},"usersSearchTerm":"","filterState":{"sortSelection":{"value":"globalrelevanceex"},"isAllHomes":{"value":True}},"isListVisible":True,"mapZoom":9},"wants":{"cat1":["listResults"],"cat2":["total"]},"requestId":11,"isDebugRequest":False}
        yield scrapy.Request(request_url, method='PUT',callback=self.parse, body=json.dumps(payload))

    def parse(self, response):
        
        response = response.json()
        list_results = response['cat1']['searchResults']['listResults']
        for result in list_results:
            print(result['detailUrl'])
        # response_dict = json.loads(response)
        # print(response_dict)

