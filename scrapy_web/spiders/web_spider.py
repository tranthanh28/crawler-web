import scrapy
from ..items import ScrapyWebItem

class WebSpiderSpider(scrapy.Spider):
    name = 'web_spider'
    allowed_domains = ['www.24h.com.vn']
#     start_urls = ['https://www.24h.com.vn/tin-tuc-trong-ngay/lien-quan-ca-tu-vong-do-benh-dai-o-me-linh-25-nguoi-da-duoc-dua-di-tiem-vaccine-c46a1408588.html']
#     start_urls = ['https://www.24h.com.vn/tin-tuc-trong-ngay/vu-100-nguoi-viet-mat-lien-lac-o-han-quoc-hang-nao-khai-thac-duong-bay-thang-toi-gangwon-c46a1408876.html']
#     start_urls = ['https://www.24h.com.vn/tin-tuc-trong-ngay/tau-ca-va-cham-voi-tau-van-tai-3-thuyen-vien-mat-tich-c46a1409219.html']
    start_urls = ['https://www.24h.com.vn/tin-tuc-trong-ngay/chieu-nay-cong-bo-tan-bi-thu-tinh-uy-hai-duong-c46a1409197.html']

    def parse(self, response):
        item = ScrapyWebItem()
        item['title'] = response.css("#article_title ::text").extract_first()
        item['describe'] = response.css('#article_sapo ::text').extract()
        item['content'] = response.css('#article_body > p ::text').extract()
        item['time'] = response.css('#article_body > div.mg20.ovf.clF.btn-share-24h-art > div.updTm.updTmD.mrT5 ::text').extract_first()
        item['author'] = response.css('#left > main > div > div.mg20.ovf.clF.btn-share-24h-art > div.nguontin.nguontinD.bld.mrT10.mrB10.fr ::text').extract_first()
        item['category'] = response.css('#left > main > div > header > div > nav:nth-child(1) > div.cateBdm.brmCmTb.brmCmTbx > ul > li > a > span ::text').extract_first()
        item['web_link'] = self.start_urls
        # .re('-\s[^\n]*\\r')
        yield item