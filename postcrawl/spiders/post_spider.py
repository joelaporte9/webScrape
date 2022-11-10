import scrapy

class PostSpider(scrapy.Spider):
    name="spyder"
    start_urls = [
        'https://books.toscrape.com/',
    ]

    def parse(self, response):
        for books in response.css('article.product_pod'):
            yield {
                'pages': books.css('a::attr(href)').getall(),
                'title': books.css(' ').get(),
                'price': books.css('p.price_color').get(),
            }

        next_page = response.css('li.next a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
        

        


        
