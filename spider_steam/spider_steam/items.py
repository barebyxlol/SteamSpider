# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderSteamItem(scrapy.Item):
    name = scrapy.Field()
    category = scrapy.Field()
    rating = scrapy.Field()
    number_of_reviews = scrapy.Field()
    release_date = scrapy.Field()
    developer = scrapy.Field()
    tags = scrapy.Field()
    price_rub = scrapy.Field()
    sale_price_rub = scrapy.Field()
    platforms = scrapy.Field()
