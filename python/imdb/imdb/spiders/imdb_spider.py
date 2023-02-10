import scrapy


class ImdbSpiderSpider(scrapy.Spider):
    name = 'imdb_spider'
    start_urls = ['http://imdb.com/']

    def parse(self, response):
    	filmes = response.css(".titleColumn")
    	titulos = response.css(".titleColumn a::text")
    	anos = response.css(".secondaryInfo ::text")
    	nota = response.css("strong::text")
        pass
