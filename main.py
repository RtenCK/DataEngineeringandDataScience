import pandas as pd
import requests
import re
from bs4 import BeautifulSoup

numberOfPages = 2

def getData(pageNumber):
    headers = {"User-Agent":"DeepCrawl", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
    # headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
    baseUrl = "https://www.yelp.com/biz/the-oxbow-hotel-eau-claire-5?start="
    completeUrl = baseUrl + str(pageNumber) + str(0)
    yelpRequest = requests.get(completeUrl, headers = headers)
    content = yelpRequest.content
    # print(content)
    soup = BeautifulSoup(content)
    # print(soup.get_text())
    # print("getting text")

    allReviews = []

    for unorederedList in soup.findAll('ul', attrs={'class':'undefined list__373c0__vNxqp'}):
        for block in unorederedList.findAll('div', attrs={'class': 'review__373c0__3MsBX border-color--default__373c0__1WKlL'}):
            reviewBlock = []
            reviewBlock.append(block.find('p', attrs={'class':'comment__373c0__Nsutg'}).text)
            rating = block.find('div', attrs={'class':'i-stars__373c0___sZu0'})['aria-label']
            rating = re.split('\s', rating)
            reviewBlock.append(rating[0])
            # print(reviewBlock)
            reviewBlock.append(block.find('span', attrs={'class':'fs-block css-m6anxm'}).text)
            allReviews.append(reviewBlock)
            print(allReviews[0])
    
    
    flatten = lambda l: [item for sublist in l for item in sublist]
    reviewDataFrame = pd.DataFrame(flatten(allReviews), columns=['Review', 'Rating', 'Author'])
# for i in range(0, numberOfPages):
getData(0)