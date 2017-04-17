import scrapy

class LoginSpider(scrapy.Spider):
    
    # This is the range which needs to be set by user
    # aa = range

    aa = 0
    xx = []
    name = 'myspider'
    start_urls = ['http://mis.mptransport.org/MPLogin/eSewa/VehicleSearch.aspx']

    def parse(self, response):

        # This is the max value of range
        if self.aa >= 1001:
            print(self.xx)
            return()
        bb = ('%.4d' % self.aa)
        return scrapy.FormRequest.from_response(
            response,
            formdata={"ctl00$ContentPlaceHolder1$txtRegNo": bb, "ctl00$ContentPlaceHolder1$RadioButtonList1": "END"},
            dont_filter = True,
            callback=self.get_details
        )

    def get_details(self, response):
        print(self.aa)
        self.xx.append(self.aa) # To show all the data which are scraped
        self.aa+=1
        bb = ('%.4d' % int(self.aa-1))
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
