import scrapy

from douban.items import DoubanMovieTop250Item


class MovieTop250Spider(scrapy.Spider):
    name = "doubanmovietop250"
    allowed_domains = ["movie.douban.com"]
    start_urls = ["https://movie.douban.com/top250"]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, dont_filter=True, callback=self.parse_urls)

    def parse_urls(self, response):
        link = response.xpath('//a[@class=""]/@href').extract()
        links = link[-1::-1]
        for url in links:
            yield scrapy.Request(url, dont_filter=True, callback=self.parse_content)
        nextlink = response.xpath('//*[@id="content"]/div/div[1]/div[2]/span[3]/link/@href').extract()
        if nextlink:
            nextlinks="https://movie.douban.com/top250"+nextlink[0]
            yield scrapy.Request(nextlinks, dont_filter=True, callback=self.parse_urls)

    def parse_content(self, response):
        item = DoubanMovieTop250Item()
        item['title'] = response.xpath('//span[@property="v:itemreviewed"]/text()').extract()
        item['type'] = response.xpath('//span[@property="v:genre"]/text()').extract()
        item['score'] = response.xpath('//strong[@property="v:average"]/text()').extract()
        item['date'] = response.xpath('//span[@property="v:initialReleaseDate"]/text()').extract()
        item['length'] = response.xpath('//span[@property="v:runtime"]/text()').extract()
        temp = response.xpath('//span[@property="v:summary"]/text()').extract()
        introduction = ''
        for i in temp:
            introduction += i.replace('\n', '').replace(' ', '').replace('\u3000', '')
        item['introduction'] = introduction
        return item
