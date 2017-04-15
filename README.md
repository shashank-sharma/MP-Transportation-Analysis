# MP-Transportation-Analysis

## Introduction

### AIM

Our aim is to gather as much data as possible from a given website and use it to analyze and then compare it.
For data we used this 'http://mis.mptransport.org/MPLogin/eSewa/VehicleSearch.aspx' site to scrape it.

NOTE: It's not recommended to scrape this site all of sudden. It was used to test my knowledge and also to gain data.

### How data is obtained?

Since the data related MP transportation was public so we used the given URL and scrape it. For scraping, python language used. It first select the field of registration number and then inputs 0000, 0001 ... 9999 just like this.

### Technical details

Python version | Python 2.7.6

Tools used was Scrapy. Whole program was successful because of scrapy project. We used this to create one spider and then deployed it on scrapinghub.com
Reason is pretty obvious because we are dealing with 10 millions of data. With single laptop it will take approx 1 month 5 days so to fasten this process we used scrapinghub.com 4 units and then scraped data.

### How to use?

At first you need to clone this repository to your local machine

git clone https://github.com/shashank-sharma/MP-Transportation-Analysis

After that move to the MP-Transportation-Analysis directory by cd and then install scrapinghub toolbelt.

pip install shub

If you find any error then install this in virtual environment.

After installing create an account in scrapinghub.com and just after that create one project by using Scrapy tool. After creating you will be redirected to new window. Now go to deploy option in left side bar menu and there at down you will see project id and API key just save them.

Now again switch to terminal and type 'shub deploy' and then enter all the details which is needed and then your project will be deployed to the scrapinghub.com. Now go to dashboard and Run it. Then it will start scraping.

For free version you might need to set some range from 0 - 1001 because max time your process will run is for 24 hours. So you might need to run your program 10 times with different range

### Data analysis

To load up data we used the JSON format rather than .db or .sql because converting JSON to these format may take 20+ days continuous operation which is not possible to handle by the system so we used Python to load JSON files and then later we did our maths to calculate our result.
