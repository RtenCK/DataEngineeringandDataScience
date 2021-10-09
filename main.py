import requests
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

    reviews = []
    ratings = []
    names = []

    for unorederedList in soup.findAll('ul', attrs={'class':'undefined list__373c0__vNxqp'}):
        for block in unorederedList.findAll('div', attrs={'class': 'review__373c0__3MsBX border-color--default__373c0__1WKlL'}):
            reviews.append(block.find('p', attrs={'class':'comment__373c0__Nsutg'}))
            ratings.append(block.find('div', attrs={'class':'i-stars__373c0___sZu0'}))
            names.append(block.find('span', attrs={'class':'fs-block css-m6anxm'}))

    print("LENGHTS")
    print(len(names))
    print(len(ratings))
    print(len(reviews))

    # for i in range(0, 10):
    #     realName = names[i].find('a')
    #     if realName is not None:
    #         print(realName.text)

    #     print(reviews[i])
    #     print(ratings[i].text)


    print ("//////////////////////////////////////")
    print ("NAMES")
    # for i in range(1, 11):
    #     realName = names[i].find('a')
    #     if realName is not None:
    #         print(realName.text)

        # print(reviews[i-1])

    # for name in names:
    #     realName = name.find('a')

    #     if realName is not None:
    #         print(realName.text)
    
    print ("//////////////////////////////////////")
    print ("REVIEWS")
    # for review in reviews:
    #     if review is not None:
    #         print(review.text)

    print ("//////////////////////////////////////")
    print ("RATINGS")
    # for rating in ratings:
    #     print(ratings)
    #     if rating is not None:
    #         print(rating.text)
# for i in range(0, numberOfPages):
getData(0)