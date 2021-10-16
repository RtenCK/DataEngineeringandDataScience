import pandas as pd
import requests
import re
from bs4 import BeautifulSoup

import nltk
import re
from nltk.corpus import stopwords                   #Stopwords corpus
from nltk.stem import PorterStemmer                 # Stemmer

from sklearn.feature_extraction.text import CountVectorizer          #For Bag of words
from sklearn.feature_extraction.text import TfidfVectorizer          #For TF-IDF

numberOfPages = 4
allReviews = []

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


    for unorederedList in soup.findAll('ul', attrs={'class':'undefined list__373c0__vNxqp'}):
        for block in unorederedList.findAll('div', attrs={'class': 'review__373c0__3MsBX border-color--default__373c0__1WKlL'}):
            reviewBlock = []
            reviewBlock.append(block.find('p', attrs={'class':'comment__373c0__Nsutg'}).text)
            rating = block.find('div', attrs={'class':'i-stars__373c0___sZu0'})['aria-label']
            rating = re.split('\s', rating)
            reviewBlock.append(rating[0])
            reviewBlock.append(block.find('span', attrs={'class':'fs-block css-m6anxm'}).text)
            allReviews.append(reviewBlock)
    

def partition(x):
    if x > 2.5:
        return 'positive'
    return 'negative'

# THIS IS FOR SCRAPING
# for i in range(0, numberOfPages):
#     getData(i)
# reviewDataFrame = pd.DataFrame(data = allReviews, columns=['Review', 'Rating', 'Author'])
# reviewDataFrame.to_csv('yelp_reviews.csv')

# READ CSV's
reviewDataFrame = pd.read_csv('yelp_reviews.csv')
print(reviewDataFrame.columns)

labelColumn = reviewDataFrame['Rating'].map(partition)
reviewDataFrame['labelColumn'] = labelColumn
print(reviewDataFrame)

final_X = reviewDataFrame['Review']
final_y = reviewDataFrame['Rating']

nltk.download('stopwords')
stop = set(stopwords.words('english'))

temp =[]

snow = nltk.stem.SnowballStemmer('english')
for sentence in final_X:
    sentence = sentence.lower()                 # Converting to lowercase
    cleanr = re.compile('<.*?>')
    sentence = re.sub(cleanr, ' ', sentence)        #Removing HTML tags
    sentence = re.sub(r'[?|!|\'|"|#]',r'',sentence)
    sentence = re.sub(r'[.|,|)|(|\|/]',r' ',sentence)        #Removing Punctuations
    
    words = [snow.stem(word) for word in sentence.split() if word not in stopwords.words('english')]   # Stemming and removing stopwords
    temp.append(words)
    
final_X = temp 

# labelColumn = reviewDataFrame.map(reviewDataFrame['Review'])