import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class RbagenciesspiderSpider(CrawlSpider):
    name = 'RBAgenciesSpider'
    allowed_domains = ['reportbeam.com']
    start_urls = ['https://www.reportbeam.com/ecommerceportal/selection.aspx']

    rules = (
        Rule(LinkExtractor(restrict_xpaths=r'//a[contains(@href, "./Selection")]'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        agencies = response.xpath('//a[contains(@href, "/Selection.aspx?agency")]/@href').getall()
        for agency in agencies:
            yield {'agency': agency}
