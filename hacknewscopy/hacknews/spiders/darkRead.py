import scrapy


class DarkreadSpider(scrapy.Spider):
    name = 'darkRead'
    allowed_domains = ['www.darkreading.com/attacks-breaches']
    start_urls = ['https://www.darkreading.com/attacks-breaches/']

    def parse(self, response):
        attacks = response.xpath("//*[@class='topic-content-article']")
        
        for item in attacks:
            name = item.xpath(".//text()").get()
            link = item.xpath(".//@href").get()
            date = item.xpath(".//*[@class='arcile-date']/text()").get() #arcile-date is website miss-spell
            yield{
                'title': name,
                'date' : date,
                'link' : link
                
            }
