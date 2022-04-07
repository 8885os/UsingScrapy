import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import codecs

from books.items import BooksItem
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst


class BookcrawlerSpider(CrawlSpider):
    name = 'BookCrawler'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    rules = (
        Rule(LinkExtractor(allow=('catalogue/category')), callback='parsepage', follow=True),
    )

    def parsepage(self, res):
        books = res.xpath('//article[@class="product_pod"]')#defines xpath selector for markup data for each book

        for b in books:
            book_loader = ItemLoader(item=BooksItem(), selector=b)#creates an instance passed in books item and the current book as selector
            book_loader.default_output_processor = TakeFirst()
            #for each field we invoke bookloader.add_xpath
            book_loader.add_xpath('title', './/h3/a/@title')
            book_loader.add_xpath('price', './/div/p[@class="price_color"]/text()')
            book_loader.add_xpath('imageurl', './/img[@class="thumbnail"]/@src')
            book_loader.add_xpath('bookurl', './/h3/a/@href')

            print('\r\n')
            #passing corresponding markup selectors
            yield book_loader.load_item()#returns every scraped book