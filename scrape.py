import urllib2
from bs4 import BeautifulSoup
import csv
import re
item = {'itemurl':None,'imageUrl':None,'sellerName':None,'name':None,'price':None}
def load_seller(sellerUrl,seller):
    quote_page=sellerUrl
    page = urllib2.urlopen(quote_page)
    soup = BeautifulSoup(page, 'html.parser')
    sellerName = seller
    container = soup.find('ul', attrs={'class':"listing-cards block-grid-xs-2 block-grid-md-3 block-grid-no-whitespace mb-xs-3"})
    with open('mycsvfile1.csv', 'a') as f:  # Just use 'w' mode in 3.x
        w = csv.DictWriter(f, item.keys())
        #w.writeheader()
        for link in container.find_all('a',attrs={'class':" display-inline-block listing-link "}):
            item1={}
            item1['itemurl'] = link.get('href').encode('utf-8')
            item1['imageUrl'] = link.find('img').get('src').encode('utf-8')
            item1['sellerName'] = sellerName.encode('utf-8')
            item1['name'] = link.find('p',attrs={'class':'text-gray text-truncate mb-xs-0 text-body'}).text.encode('utf-8').strip()
            item1['price'] = link.find('span',attrs={'class':'currency-value'}).text.encode('utf-8').strip()
            
            w.writerow(item1)
def load(urls):
    open('mycsvfile1.csv', 'w').close()
    with open('mycsvfile1.csv', 'a') as f: 
        w = csv.DictWriter(f, item.keys())
        w.writeheader()
    for i in range(len(urls)):
        print i
        print urls[i]
        matchObj = re.match( r'https://www.etsy.com/shop/(\w+)?.*', urls[i], re.M|re.I)
        load_seller(urls[i],matchObj.group(1))