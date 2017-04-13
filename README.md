# MP-Transportation-Analysis

## Introduction

###AIM

Our aim is to gather as much data as possible from a given website and use it to analyze and then compare it.
For data we used this 'http://mis.mptransport.org/MPLogin/eSewa/VehicleSearch.aspx' site to scrape it.

NOTE: It's not recommended to scrape this site all of sudden. It was used to test my knowledge and also to gain data.

###How data is obtained?

Since the data related MP transportation was public so we used the given URL and scrape it. For scraping, python language used. It first select the field of registration number and then inputs MP01 MP02 ... MP99 just like this and makes every requests and then saves data in respective .txt files.

###Technical details

Python version | Python 2.7.6

Modules used | BeautifulSoup, Mechanize, plotly


In total there are 2 python programs used.

####scrape.py

This is used to scrape the given site. Total request which were made is 100. Also this program is responsible for data creation in their respective .txt files. So in total it will create 13 files for later use.

####main.py

This program is used to open respective .txt files and then manipulate those data to show result according to our needs.

###How to use?

At first you need to clone this repository to your local machine

git clone https://github.com/shashank-sharma/MP-Transportation-Analysis

After that at first you need to run scrape.py, so first change your directory to this folder and then type

python scrape.py

This process might take so much of time, or it might take even 1 day to complete because of late response from server also it have loads of data.(For me it was completed after 20 hours. NOTE: you can greatly increase its performance by using multiprocessing concept.)
After completion of this process run main.py file to get results.

python main.py

And that's how we scrape, manipulate and get results.



If there is any issue regarding this program, or is there anything which can be changed then please do.
