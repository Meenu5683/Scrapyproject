import scrapy


class CarbonSpider(scrapy.Spider):
    name = "carbon"
    allowed_domains = ['carbon38.com']
    page_number = 2

    start_urls = ["https://carbon38.com/en-in/collections/tops?category_id=273980817597&category_url=%2Fcollections%2Ftops"]

    li=[]
    for i in range(2,10):
        a='https://carbon38.com/en-in/collections/tops?category_id=273980817597&category_url=%2Fcollections%2Ftops&page_num='+str(page_number)
        if page_number < 10:
            page_number += 1
        li.append(a)


    def parse(self, response):
        profile_page_links = response.xpath("//a[@class='isp_product_image_href']/@href").extract()
        yield from response.follow_all(profile_page_links, self.parse_profile)

        next_page = CarbonSpider.li
        yield from response.follow_all(next_page, self.parse)

    def parse_profile(self, response):
        def extract_with_xpath(query):
            return response.xpath(query).get(default="").strip()


        yield {
            "product_name":extract_with_xpath("//h1/text()")
        }


