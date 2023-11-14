# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class FilmItem(scrapy.Item):
    """
    Item for storing film data
    """

    url = scrapy.Field()
    name = scrapy.Field()
    score = scrapy.Field()
    top_rate = scrapy.Field()
    year = scrapy.Field()
    length = scrapy.Field()
    popularity = scrapy.Field()
    storyline = scrapy.Field()
    genres = scrapy.Field()
    writers = scrapy.Field()
    directors = scrapy.Field()
    budget = scrapy.Field()
    gross_worldwide = scrapy.Field()
    origin_countries = scrapy.Field()
    origin_language = scrapy.Field()
    production_companies = scrapy.Field()
    wins = scrapy.Field()
    nominations = scrapy.Field()
    cast = scrapy.Field()
