import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class RbagenciesspiderSpider(CrawlSpider):
    name = 'RBAgenciesSpider'
    allowed_domains = ['reportbeam.com']
    start_urls = ['https://www.reportbeam.com/ecommerceportal/selection.aspx']

    rules = (
        Rule(LinkExtractor(restrict_xpaths=r'//a[contains(@href, "./Selection.aspx?state")]'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        agencies = response.css('table#ctl00_cplhMainContent_grdAgencySelection tr:not(.grd_Heading)')
        for agency in agencies:
            yield {
                'AgencyName': agency.xpath('./td/text()').getall()[0],
                'WebsiteAgencyName': agency.xpath('.//a/@href').get()
            }
