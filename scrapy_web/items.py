# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyWebItem(scrapy.Item):
    # define the fields for your item here like:

    web_link = scrapy.Field()
    web_domain_name = scrapy.Field()
    title = scrapy.Field()
    describe =scrapy.Field()
    content = scrapy.Field()
    time = scrapy.Field()
    author = scrapy.Field()
    category = scrapy.Field()
