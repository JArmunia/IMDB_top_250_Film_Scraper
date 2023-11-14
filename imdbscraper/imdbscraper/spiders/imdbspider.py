import scrapy
from imdbscraper.items import FilmItem
import random
import fake_useragent


class ImdbspiderSpider(scrapy.Spider):
    """
    Spider for scraping film data from imdb.com
    """

    name = "imdbspider"
    allowed_domains = ["imdb.com"]
    start_urls = ["https://www.imdb.com/chart/top/?ref_=nv_mv_250"]

    def parse(self, response):
        film_relative_urls = response.css(
            ".ipc-metadata-list-summary-item__tc a::attr(href)")
        for film_relative_url in film_relative_urls:

            film_url = "https://www.imdb.com/" + film_relative_url.get()

            resp = response.follow(film_url,
                                   callback=self.parse_film,
                                   )
            yield resp

    def parse_film(self, response):

        name = response.xpath(
            '//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[2]/div[1]/h1/span/text()').get()
        score = response.xpath(
            '//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[2]/div[2]/div/div[1]/a/span/div/div[2]/div[1]/span[1]/text()').get()
        top_rate = response.xpath(
            '//*[@id="__next"]/main/div/section[1]/div/section/div/div[1]/section[1]/div/div/a/text()').get()

        year = response.xpath(
            '//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[2]/div[1]/ul/li[1]/a/text()').get()
        length = response.xpath(
            '//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[2]/div[1]/ul/li[3]/text()').get()
        popularity = response.xpath(
            '//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[2]/div[2]/div/div[3]/a/span/div/div[2]/div[1]/text()').get()
        storyline = response.xpath(
            '//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/section/p/span[3]/text()').get()

        genre_query = '//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/section/div[1]/div[2]/a'
        genres = []
        for a in response.xpath(genre_query):
            genre = a.xpath('normalize-space(.)').get()
            genres.append(genre)

        writers_query = '//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/section/div[2]/div/ul/li[2]/div/ul/li'
        writers = []
        for li in response.xpath(writers_query):
            writer = li.xpath('normalize-space(.)').get()
            writers.append(writer)

        directors_query = response.xpath(
            '//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/section/div[2]/div/ul/li[1]/div/ul/li')
        directors = []
        for li in directors_query:
            director = li.xpath('normalize-space(.)').get()
            directors.append(director)

        budget = response.xpath(
            '//*[@id="__next"]/main/div/section[1]/div/section/div/div[1]/section[11]/div[2]/ul/li[1]/div/ul/li/span/text()').get()
        gross_worldwide = response.xpath(
            '//*[@id="__next"]/main/div/section[1]/div/section/div/div[1]/section[11]/div[2]/ul/li[4]/div/ul/li/span/text()').get()

        origin_countries_query = response.xpath(
            '//*[@id="__next"]/main/div/section[1]/div/section/div/div[1]/section[10]/div[2]/ul/li[2]/div/ul/li')
        origin_countries = []
        for li in origin_countries_query:
            origin_country = li.xpath('.//a/text()').get()
            origin_countries.append(origin_country)

        origin_language = response.xpath(
            '//*[@id="__next"]/main/div/section[1]/div/section/div/div[1]/section[10]/div[2]/ul/li[4]/div/ul/li/a/text()').get()

        companies_query = response.xpath(
            '//*[@id="__next"]/main/div/section[1]/div/section/div/div[1]/section[10]/div[2]/ul/li[7]/div/ul/li')
        production_companies = []
        for li in companies_query:
            production_company = li.xpath('.//a/text()').get()
            production_companies.append(production_company)

        wins = response.xpath(
            '//*[@id="__next"]/main/div/section[1]/div/section/div/div[1]/section[1]/div/ul/li/div/ul/li/span/text()').get()
        nominations = response.xpath(
            '//*[@id="__next"]/main/div/section[1]/div/section/div/div[1]/section[1]/div/ul/li/a[1]/text()').get()

        if not response.xpath('//*[@id="__next"]/main/div/section[1]/div/section/div/div[1]/section[4]/div[2]/div[2]/div/div[2]/a/text()').get() is None:
            cast_table_query = response.xpath(
                '//*[@id="__next"]/main/div/section[1]/div/section/div/div[1]/section[4]/div[2]/div[2]/div')
            cast = []
            for li in cast_table_query:
                actor = li.xpath('./div[2]/a/text()').get()
                role = li.xpath('./div[2]/div/ul/li/a/span/text()').get()
                cast.append({"actor": actor, "role": role})
        else:
            cast_table_query = response.xpath(
                '//*[@id="__next"]/main/div/section[1]/div/section/div/div[1]/section[3]/div[2]/div[2]/div')
            cast = []

            for div in cast_table_query:
                actor = div.xpath('./div[2]/a/text()').get()
                role = div.xpath('./div[2]/div/ul/li/a/span/text()').get()
                cast.append({"actor": actor, "role": role})

        film = {
            "url": response.url,
            "name": name,
            "score": score,
            "top_rate": top_rate,
            "year": year,
            "length": length,
            "popularity": popularity,
            "storyline": storyline,
            "genres": genres,
            "writers": writers,
            "directors": directors,
            "budget": budget,
            "gross_worldwide": gross_worldwide,
            "origin_countries": origin_countries,
            "origin_language": origin_language,
            "production_companies": production_companies,
            "wins": wins,
            "nominations": nominations,
            "cast": cast,
        }

        film_item = FilmItem()
        film_item["url"] = film["url"]
        film_item["name"] = film["name"]
        film_item["score"] = film["score"]
        film_item["top_rate"] = film["top_rate"]
        film_item["year"] = film["year"]
        film_item["length"] = film["length"]
        film_item["popularity"] = film["popularity"]
        film_item["storyline"] = film["storyline"]
        film_item["genres"] = film["genres"]
        film_item["writers"] = film["writers"]
        film_item["directors"] = film["directors"]
        film_item["budget"] = film["budget"]
        film_item["gross_worldwide"] = film["gross_worldwide"]
        film_item["origin_countries"] = film["origin_countries"]
        film_item["origin_language"] = film["origin_language"]
        film_item["production_companies"] = film["production_companies"]
        film_item["wins"] = film["wins"]
        film_item["nominations"] = film["nominations"]
        film_item["cast"] = film["cast"]
        yield film_item
