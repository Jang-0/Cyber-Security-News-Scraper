import scrapy


class HacknewsSpider(scrapy.Spider):
    name = 'hackNews'
    allowed_domains = ['thehackernews.com/search/label/Cyber%20Attack']
    start_urls = ['https://thehackernews.com/search/label/Cyber%20Attack/']

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
