import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'quotes' # nombre de nuestra clase
    start_urls = ['http://quotes.toscrape.com/'] # la dirección web a la que se va a apuntar

    def parse(self, response): 
        '''Este metodo es el que define la logica a partir de la cual nosotros extraemos información.
        -self: hace referencia a la instancia posterior de una clase.
        -response: hace referencia a la respuesta http'''
        
        with open('resultados.html', 'w', encoding='utf-8') as f:
            f.write(response.text)