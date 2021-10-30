import scrapy


class HacknewsmalSpider(scrapy.Spider):
    name = 'hackNewsMal'
    allowed_domains = ['thehackernews.com/search/label/Malware']
    start_urls = ['https://thehackernews.com/search/label/Malware/']

    def parse(self, response):
        attacks = response.xpath('//*[@class="story-link"]')
        
        for item in attacks:
            name = item.xpath(".//h2/text()").get()
            link = item.xpath(".//@href").get()
            date = item.xpath('.//*[@class="item-label"]/text()').get()
            yield{
                'title': name,
                'date' : date,
                'link' : link
            }