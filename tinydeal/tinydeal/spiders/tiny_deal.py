import scrapy


class TinyDealSpider(scrapy.Spider):
    name = "tiny_deal"
    allowed_domains = ["web.archive.org"]
    start_urls = ['https://web.archive.org/web/20190225123327/https://www.tinydeal.com/specials.html']
    

    def parse(self, response):
        for product in response.xpath('//ul[@class="productlisting-ul"]/div/li'):
            
            yield{
                'title': product.xpath('.//a[@class="p_box_title"]/text()').get(),
                'url': response.urljoin(product.xpath('.//a[@class="p_box_title"]/@href').get()),
                'discounted_price': product.xpath('.//div[@class="p_box_price"]/span[1]/text()').get(),
                'original_price': product.xpath('.//div[@class="p_box_price"]/span[2]/text()').get()
            }