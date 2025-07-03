from bs4 import BeautifulSoup
import re
import requests
from time import gmtime, strftime

a = []
url_str = "computer"
url = []

words = url_str.split()
var = len(words)

if var == 1:
    url = "https://www.amazon.com/s/ref=nb_sb_noss_1?url=search-alias%3Daps&field-keywords=" + \
        words[0]

if var == 2:
    url = "https://www.amazon.com/s/ref=nb_sb_noss_1?url=search-alias%3Daps&field-keywords=" + \
        words[0] + "+" + words[1]

elif var == 3:
    url = "https://www.amazon.com/s/ref=nb_sb_noss_1?url=search-alias%3Daps&field-keywords=" + \
        words[0] + "+" + words[1] + "+" + words[2]

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; MaheshSpidey/1.3; +https://maheshdhingra.xyz)"
}

r = requests.get(url, headers=HEADERS)


soup = BeautifulSoup(r.content, "html.parser")

filename = "data/products.csv"
f = open(filename, "w", encoding='utf-8')

strftime("%Y-%m-%d %H:%M:%S", gmtime())

headers = "Asin, Name," + "Price : " + \
    strftime("%Y-%m-%d %H:%M:%S", gmtime()) + ", Number of Reviews\n"
f.write(headers)


containers1 = soup.findAll(
    "li", {"class": "s-result-item s-result-card-for-container a-declarative celwidget "})
print("containers style 1: ", len(containers1))

containers2 = soup.findAll(
    "li", {"class": "s-result-item s-result-card-for-container s-carded-grid celwidget "})
print("containers style 2: ", len(containers2))

sponsored_containers = soup.findAll(
    "li", {"class": "s-result-item celwidget AdHolder"})
print("containers style 3 sponsored: ", len(sponsored_containers))

common_containers = soup.findAll("li", {"class": "s-result-item celwidget "})
print("containers style 4 common: ", len(common_containers))

containers3 = soup.findAll(
    "li", {"class": "s-result-item s-col-span-12 celwidget "})
print("containers style 5 special", len(containers3))


for container in sponsored_containers:
    asin = (container["data-asin"])

    try:
        title_container = container.findAll(
            "a", {"class": "a-link-normal s-access-detail-page s-color-twister-title-link a-text-normal"})
        name = title_container[0]["title"]
    except:
        name = "N/A"

    price_container = container.findAll("span", {"class": "a-offscreen"})
    price = price_container[1].text

    num_review_container = container.findAll(
        "a", {"class": "a-size-small a-link-normal a-text-normal"})
    try:
        if (len(num_review_container) > 1):
            num_reviews = num_review_container[1].text
        else:
            num_reviews = num_review_container[0].text
    except:
        num_reviews = "0"


for container in common_containers:
    asin = (container["data-asin"])

    try:
        title_container = container.findAll(
            "a", {"class": "a-link-normal s-access-detail-page s-color-twister-title-link a-text-normal"})
        name = title_container[0]["title"]
    except:
        name = "N/A"

    price_container = container.findAll("span", {"class": "a-offscreen"})
    try:
        price = price_container[0].text
    except:
        price = "N/A"

    num_review_container = container.findAll(
        "a", {"class": "a-size-small a-link-normal a-text-normal"})
    try:
        if (len(num_review_container) > 1):
            num_reviews = num_review_container[1].text
        else:
            num_reviews = num_review_container[0].text
    except:
        num_reviews = "0"

    f.write(asin + ',' + name.replace(",", "|") + ',' +
            price.replace("$", "") + "," + num_reviews.replace(",", "") + "\n")

f.close()
