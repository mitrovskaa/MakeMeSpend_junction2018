'''
    Done by: Henok Seifu
    Generate n number of customers randomly, with
    random tags and location. 
'''

import json
import random

def generate(n, tagged=True):
    merchants = []
    for i in range(n):
        merchant = {}
        merchant["id"] = "m"+str(i)
        merchant["name"] = "merchant_"+str(i+1)
        merchant["location"] = random.randint(1000,9999)
        merchant["category"] = ["clothes","food","drinks","entertainment"][random.randrange(4)]
        merchant["price_cat"] = random.randint(1,5)
        tags = []
        if merchant["category"] == "closthes":
            tags = random.sample(["pants", "dresses", "shorts", "stockings", "t-shirts", "shirts", "suites", "ties"],4)
        elif merchant["category"] == "food":
            tags = random.sample(["burger", "cheese burger", "fries", "fish", "sandwich", "chicken", "beef", "pork"],4)
        elif merchant["category"] == "drinks":
            tags = random.sample(["coffee", "soft drinks", "beer", "wine", "whisky", "tea", "cappuccino", "water"],4)
        else:
            tags = random.sample(["movies", "snow boarding", "sauna", "games", "vaccation", "flights", "swimming", "gym"],4)
        if tagged:
            merchant["tags"] = tags
        else:
            merchant["tags"] = []
        merchants.append(merchant)

    fp = open("merchants.json", 'w')
    json.dump(merchants, fp)
    fp.close()