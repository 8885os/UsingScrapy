
import scrapy
from scrapy.loader.processors import MapCompose

def addlink(url):
    return 'https://books.toscrape.com/' + url.replace('../', '')

class BooksItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    imageurl = scrapy.Field(
        input_processor = MapCompose(addlink)# formats the url for the image url before the values are assigned

    )
    bookurl = scrapy.Field(
        input_processor = MapCompose(addlink)
    )

