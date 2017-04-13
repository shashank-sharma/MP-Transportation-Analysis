import scrapy
from scrapy.utils.response import open_in_browser

aa = 0

class LoginSpider(scrapy.Spider):
    name = 'myspider'
    start_urls = ['http://mis.mptransport.org/MPLogin/eSewa/VehicleSearch.aspx']

    def parse(self, response):
        global aa
        if aa >= 1001:
            return()
        bb = ('%.4d' % aa)
        return scrapy.FormRequest.from_response(
            response,
            formdata={"ctl00$ContentPlaceHolder1$txtRegNo": bb, "ctl00$ContentPlaceHolder1$RadioButtonList1": "END"},
            dont_filter = True,
            callback=self.get_details
        )

    def get_details(self, response):
        global aa
        aa+=1
        bb = ('%.4d' % int(aa-1))
        a = response.css('table.Grid tr')[1:-1]
        if len(a) == 0:
            yield scrapy.Request(
                url="http://mis.mptransport.org/MPLogin/eSewa/VehicleSearch.aspx",
                dont_filter = True,
                callback=self.parse
            )
            return
        for i in a:
            registrationNo = i.css('td a::text').extract_first() 
            chassisNo, engineNo, ownerName, rtoName, manufacturingYear, regisDate, ownerNo, issuedOn, colour, TClass, maker, model = i.css('td::text')[1:].extract()
            yield {
                'RegistrationNo:': registrationNo,
                'ChassisNo': chassisNo,
                'EngineNo': engineNo,
                'OwnerName': ownerName,
                'RTOName': rtoName,
                'ManufacturingYear': manufacturingYear,
                'RegistrationDate': regisDate,
                'OwnerNo': ownerNo,
                'IssuedOn': issuedOn,
                'Colour': colour,
                'Class': TClass,
                'Maker': maker,
                'Model': model,
            }
        yield scrapy.Request(
            url="http://mis.mptransport.org/MPLogin/eSewa/VehicleSearch.aspx",
            dont_filter = True,
            callback=self.parse
        )

'''

        Data representation used in website:
        Note: Important data is represented by (*)
        table   | Values
        ---------------------------------
        0       | Sno
        1       | Reg Details (image)
        2       | Registration number
        3       | Chassis No
        4       | Engine no
        5       | Owner Name
        6       | RTO Name*
        7       | Manufacturing year
        8       | Registration date
        9       | Owner no
        10      | Issued on
        11      | Colour*
        12      | Class*
        13      | Maker*
        14      | Model*

'''

'''
import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser

class myspiderSpider(scrapy.Spider):
    name = "myspider"
    allowed_domains = ["http://mis.mptransport.org/MPLogin/eSewa/VehicleSearch.aspx"]

    def start_requests(self):
        return [ FormRequest("http://mis.mptransport.org/MPLogin/eSewa/VehicleSearch.aspx",
                     formdata={"ctl00$ContentPlaceHolder1$txtRegNo": "MP68G0001"},
                     callback=self.parse) ]

    def parse(self, response):
        open_in_browser(response)
        for quote in response.css('a::attr(href)').extract():
            yield {
                'url': quote,
            }

'''


'''
import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        url = 'http://quotes.toscrape.com'
        tag = getattr(self, 'tag', None)
        if tag is not None:
            url = url + 'tag/' + tag
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('small.author::text').extract_first(),
            }

        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, self.parse)
'''