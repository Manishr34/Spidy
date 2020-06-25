import scrapy
from scrap.items import ScrapItem
class scrap(scrapy.Spider):
    name = "spidy"
    start_urls = [
    "https://www.thegreenjournal.com/issue/S0167-8140(15)X0003-X?page=34",
    "https://www.sciencedirect.com/journal/annals-of-oncology/vol/29/suppl/S7"
    ]
    def parse(self,response):
        for i in response.xpath("//ol/li/ol/li/dl"):
            item = ScrapItem()
            item["author"] = i.xpath('dd/div/text()').extract()
            item["pdf_link"] = i.xpath("dd/a/@href").extract()
            item["title"] = i.xpath("dt/h3/a/span/span/text()").extract()
            yield item

        for i in response.xpath("//form/ul/ul/div/li/div/div"):
            item = ScrapItem()
            item["title"] = i.xpath("div/h4/a/text()").extract()
            item["pdf_link"] = i.xpath("div/a/@href").extract()
            item["author"] = i.xpath("div[@class='authors']/text()").extract()
            yield item
