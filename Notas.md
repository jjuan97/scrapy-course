[TOC]

# Scrapy
*version*: 2.5.0

Es un framework de alto nivel para realizar web scraping y crawling (capturar links dentro de una pagina e indexarlos para ir link por link llegando a otros sitiós).

Algo que nos permite Scrapy es extraer la información de manera estructurada, por ejemplo, se podría implementar una técnica llamada data mining en al cual se va buscando los datos para nutrir una aplicación web.

### Particularidades:
- Framework Asincrono :zap:.
- Procesador de XPath interno :arrows_clockwise:.
- Tiene shell interactiva :computer:.
- Exportar información en el formato que queramos :spiral_notepad:.
- Respeta el archivo robots.txt :robot:.

## Ejemplo scrapy *hello_world/quotes_spider.py*

Para este ejemplo vamos a crear nuestro primer scraper haciendo uso de la pagina [Quotes to scrape](anaconda3/envs/scraping/lib/python3.8/site-packages/scrapy). En ella obtendremos todo el documento html para poder observar las citas y autores.

Para inicializar un proyecto de scrapy ejecutamos en el terminal el siguiente codigo:

```bash
scrapy startproject <nombreprojecto>
```

Al finalizar tendremos una cantidad de archivos en el siguiente [Directorio archivo](./src/hello_world/tutorial/tutorial/spiders).

Para ejecutar el codigo python en scrapy tenemos que insertar en el terminal lo siguiente:

```bash
scrapy crawl quotes
```

Al ejecutar el anterior comando podemos notar que se creo un  archivo *resultados.html*.

## scrapy sheel

Para entrar en el sheel de scrapy necesitamos ejecutar en el terminal y dentro de la carpeta */tutorials/* el siguiente comando:
```bash
scrapy shell 'http:www.direccionweb.dominio'
```

Se abrira un interprete de python en el que podemos interctuar con metodos de scrapy

Para el ejemplo de **quotes to scrap** vamos a obtener el titulo:

```python
>>> response.xpath('//h1/a/text()').get()
```

Ahora vamos a obtener todas las citas:


```python
>>> response.xpath('//span[@class="text" and @itemprop="text"]/text()').getall()
```

En scrapy tambien encontramos otros metodos ademas de *response*, por ejemplo *request*:

- <span style="color:purple">request.encoding</span>, obtiene el encoding de la petición, en el caso de **quotes to scrap** sera utf-8
- <span style="color:purple">request.method</span>, trae el metodo en el que se obtiene la petición.
- <span style="color:purple">response.status</span>, trae el codigo de estado.
- <span style="color:purple">response.headers</span>, accederemos a las cabeceras http del servidor.
- <span style="color:purple">response.body</span>, el cuerpo de la respuesta.

## quotes_scraper project

En la carpeta **quotes_scraper** inicializaremos el proyecto:

```bash
scrapy startproject quotes_scraper
```

Los archivos que aparecen una vez inicializado el proyecto son:

- **scrapy.cfg:** En este archivo se encuentra la información para realizar un posterior deploy.
- **pipelines.py**: Archivo que permite modificar nuestros datos dese que entran a nuestro spider hasta llegar al final.
- **middlewares.py**: Archivo que nos permite trabajar con un concepto denominado *señales*.
- **items.py**: Es donde podemos transformar y jugar con los datos que son enviados por la respuesta html-
- **\_\_init\_\_.py**: define que todo esto es un modulo de python.
- **/spiders/**: carpeta donde vamos a colocar nuestros scripts.
- **settings.py**: Configuraciónes de scrapy de interes
  - BOT_NAME: el nombre del robot que va a usar scrapy para referirse a si mismo dentro de estas request.
  - ROBOTSTXT_OBEY: define si se va a respetar el archivo robots.txt.
  - CONCURRENT_REQUESTS: cuantas peticiones son definidas al tiempo, esto se debe a que scrapy es asincrono.
  - DOWNLOAD_DELAY: que tiempo espera scrapy entre recargas.
  - Entre otras configuraciones.

### Spiders:
Es una clase de python donde es definida la logica necesaria para extraer información.

### Creacion de los spiders
Para crear un spider basta con solo crear un nuevo archivo .py que tenga inicializado una clase extendida de scrapy.Spider. Posteriormente añadirle la logica en la funcion parse (ver [archivo](./src/quotes_scraper/quotes_scraper/quotes_scraper/spiders/) para mas info).

### Guardado de los datos

Hay mucha cantidad de archivos en los que podemos guardar: JSON, CSV, TXT, etc.
Para guardar un archivo debemos colocar el comando:
```bash
scrapy crawl quotes -o <archivo.extension>
```
:warning: importante, ejecutar este comando en la carpeta donde esta iniciado el proyecto.

Si no queremos ejecutar el comando para guardar la información y deseamos solo ejecutar **scrapy crawl \<proyecto\>** tenemos que añadir en la clase del spider el siguiente diccionario:
```python
custom_settings = {'FEED_URI': 'quotes.json', 'FEED_FORMAT': 'json'}
```

## Seguir links

Muchas veces necesitamos obtener archivos que estan en diferentes paginas, para esto necesitamos una estrategia que permita extraer el atributo href de los botones o links.

Ejemplo en **quotes to scrap**, click en el boton next.

```Python
response.xpath('//ul[@class="pager"]/li[@class="next"]/a/@href').get()
```

En la ventana de comandos de scrapy podemos movernos con la función fetch('\<link a moverse\>')

## Multiples callbacks
En scrapy se pueden generar distintos metodos de tipo parse para lograr agregar logica que corriga a pequeños problemas en los codigos.

## Pasando argumentos
Para pasar argumentos que luego python con su metodo **getattr** pueda reconocer en el codigo necesitamos mandar el flag -a en la ejecucion de scrapy:
Ejemplo:
```bash
scrapy crawl quotes -a top=5
```