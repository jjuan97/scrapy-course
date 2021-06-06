import scrapy

# Title = //h1/a/text()
# quotes = //span[@class="text" and @itemprop="text"]/text()
# author = //small[@class="author" and @itemprop="author"]/text()
# Top tags = //div[contains(@class, "tags-box")]//span[@class="tag-item"]/a/text()
# Next page button = //ul[@class="pager"]/li[@class="next"]/a/@href

# Creacion de los spiders
class QuotesSpider(scrapy.Spider):
    name = 'quotes' #nonbre unico con el que scrapy se va a referir a este spider (no debe ser repetible)
    start_urls = ['http://quotes.toscrape.com/']
    # Guardado de los datos
    #custom_settings = {'FEED_URI': 'quotes.json', 'FEED_FORMAT': 'json'} # Si no queremos ejecutar el comando para guardar la información descomentamos este codigo
    custom_settings = {'FEED_URI': 'quotes.json', 
                       'FEED_FORMAT': 'json', 
                       'CONCURRENT_REQUESTS': 24, 
                       'MEMUSAGE_LIMIT_MB': 2048,
                       'MEMUSAGE_NOTIFY_MAIL': ['juanjosechepe@gmail.com'],
                       'ROBOTSTXT_OBEY': True,
                       'USER_AGENT': 'Mmind',
                       'FEED_EXPORT_ENCODING':'utf-8'}

    # definiremos el metodo obligatorio parse (parse significa analizar un archivo para extraer información valiosa)
    '''
    def parse(self, response):
        
        #Ejemplo para visualizar lo que obtenemos en el terminal si ejecutamos desde la carpeta ./quotes_scraper/quotes_scraper el comando
        #scrapy crawl quotes


        print('\n\n')
        print('*'*15)
        print('\n\n')
        
        #print(response.status, response.headers)
        title = response.xpath('//h1/a/text()').get()
        print(f'Titulo: {title}')
        print('\n\n')
        
        quotes = response.xpath('//span[@class="text" and @itemprop="text"]/text()').getall()
        print('Citas: \n')
        for quote in quotes:
            print(f'- {quote}')
        print('\n')

        toptentags = response.xpath('//div[contains(@class, "tags-box")]//span[@class="tag-item"]/a/text()').getall()
        print('Top 10 tags: \n')
        for tag in toptentags:
            print(f'- {tag}')
        
        print('\n')


        print('*'*15)
        print('\n\n')

        '''

    # Multiples callbacks
    def parse_only_quotes(self,response, **kwargs):
        if kwargs:
            quotes = kwargs['quotes']
            authors = kwargs['authors']
        quotes.extend(response.xpath('//span[@class="text" and @itemprop="text"]/text()').getall())
        authors.extend(response.xpath('//small[@class="author" and @itemprop="author"]/text()').getall())

        next_page_button_link = response.xpath('//ul[@class="pager"]/li[@class="next"]/a/@href').get()
        if next_page_button_link: #Comprobar si el boton existe
            yield response.follow(next_page_button_link, callback=self.parse_only_quotes, cb_kwargs={'quotes': quotes, 'authors': authors})
        else:
            yield {'quotes':quotes, 'authors': authors}

    def parse(self, response):
        '''
        Con el comando: scrapy crawl quotes -o quotes.json 
        obtendremos un archivo json (podemos cambiar por otro formato que queramos) con todo lo obtenido a continuación.
        
        Scrapy tiene un problema y es que si volvemos a ejecutar el comando el hara un append al archivo ya generado,
        por lo tanto si queremos solucionar un error sera mejor borrar el anterior archivo generado.
        '''
        title = response.xpath('//h1/a/text()').get()
        quotes = response.xpath('//span[@class="text" and @itemprop="text"]/text()').getall()
        authors = response.xpath('//small[@class="author" and @itemprop="author"]/text()').getall()
        top_tags = response.xpath('//div[contains(@class, "tags-box")]//span[@class="tag-item"]/a/text()').getall()

        # Pasando argumentos
        top = getattr(self, 'top', None) # si existe en la ejecucion un atributo de nombre top, voy a guardarlo dentro de la variable top
        if top:
            top = int(top)
            top_tags = top_tags[:top]

        yield {'title':title,
               #'quotes': quotes,
               'top_tags':top_tags}

        # Seguir links
        next_page_button_link = response.xpath('//ul[@class="pager"]/li[@class="next"]/a/@href').get()
        if next_page_button_link: #Comprobar si el boton existe
            yield response.follow(next_page_button_link, callback=self.parse_only_quotes, cb_kwargs={'quotes': quotes, 'authors': authors}) #Seguir ese link
