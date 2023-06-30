import scrapy


class CarbonSpider(scrapy.Spider):
    name = "carbon"
    allowed_domains = ['carbon38.com']


    start_urls = ["https://carbon38.com/en-in/collections/tops?category_id=273980817597&category_url=%2Fcollections%2Ftops"]


    def parse(self, response):
        profile_page_links = response.xpath("//a[@class='isp_product_image_href']/@href").extract()
        yield from response.follow_all(profile_page_links, self.parse_profile)


    def parse_profile(self, response):
        def extract_with_xpath(query):
            return response.xpath(query).get(default="").strip()
        
        yield {
            "product_name":extract_with_xpath("//h1/text()")}


