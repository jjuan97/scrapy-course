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

[Directorio archivo](./src/hello_world/tutorial/tutorial/spiders)

Para ejecutar el codigo python en scrapy tenemos que insertar en el terminal lo siguiente:

```bash
scrapy crawl quotes
```

Al ejecutar el anterior comando podemos notar que se creo un  archivo *resultados.html* .