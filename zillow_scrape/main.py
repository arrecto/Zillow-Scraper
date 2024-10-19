from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from zillow_scrape.spiders.class_spiders import ListingSpider

def main():
    settings = get_project_settings()
    process = CrawlerProcess(settings)
    process.crawl(ListingSpider)
    process.start()

if __name__ == '__main__':
    main()