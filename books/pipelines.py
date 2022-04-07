from scrapy.exceptions import DropItem


class BooksPrice(object):
    def process_item(self, item, spider):#checks if the value is expensive if it is replace the value to expensive
        price = item['price'].replace('£', '')
        if float(price) > 50:
            item['price'] = "Expensive"
        else:
            item['price'] = price
        return item

class CheckAsViable(object):#checks if the book price isnt Expensive 
    def process_item(self,item,spider): # if the price isnt expensive print the book details
        if item['price'] != "Expensive":     

            print('\r\n Book found ->')
            print('title: ' +item['title'])
            print('price: ' + item['price'])
            print('imageurl: ' + item['imageurl'])
            print('bookurl: ' + item['bookurl'])
        else:
            raise DropItem()
    
        return item

