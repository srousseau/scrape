# -*- coding: utf-8 -*-
'''
srousseau
web scraper for specific file types
scrapes 100 files at a time
saved files to downloaded folder
'''
from bs4 import BeautifulSoup
import urllib, urllib2, sys

def google_scrape(search_seed, document_type):
    address = 'http://www.google.com/search?q=%s&num=100&hl=en&start=0' % (urllib.quote_plus(search_seed + 'filetype:' + document_type))
    request = urllib2.Request(address, None, {'User-Agent':'Mosilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11'})
    urlfile = urllib2.urlopen(request)
    page = urlfile.read()
    soup = BeautifulSoup(page)

    download_links = []
    count = 0

    for li in soup.findAll('li', attrs={'class':'g'}):
        new_name = "downloaded/downloaded_" + str(count) + "." + document_type
        sLink = li.find('a')
        
        try:
            urllib.urlretrieve(sLink['href'], new_name)
            print "Downloaded " + sLink['href']
        except:
            print "Failed download of query "
            print sLink['href']
        count = count + 1
        
    return download_links
    
if __name__ == '__main__':

    total = len(sys.argv)
    if total != 3:
        print "Usage: arguement1=search seed, arguemnt2=document type"
        print "Example: python gscrape.py resume docx"
    else:
        search_seed = str(sys.argv[1])
        document_type = str(sys.argv[2])
        print "Downloading 100 files of type ." + document_type + " using seed " + search_seed
        links = google_scrape(search_seed, document_type)
