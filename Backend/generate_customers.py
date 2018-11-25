'''
    Done by: Henok Seifu
    Generate n number of customers randomly, with
    random tags and location. 

'''
import json
import random

def generate(n, tagged=True):
    customers = []
    for i in range(n):
        customer = {}
        customer["id"] = "c"+str(i)
        taggable = ["pants", "dresses", "shorts", "stockings", "t-shirts", "shirts", "suites", "ties",
        "burger", "cheese burger", "fries", "fish", "sandwich", "chicken", "beef","pork",
        "coffee", "soft drinks", "beer", "wine", "whisky", "tea", "cappuccino",
        "movies", "snow boarding", "sauna", "games", "vaccation", "flights", "swimming","gym"]
        if tagged:
            customer["tags"] = random.sample(taggable,4)
        else:
            customer["tags"] = []
        customer["name"] = "customer_"+str(i+1)
        customer["location"] = random.randint(1000,9999)
        customers.append(customer)


    fp = open("customers.json", 'w')
    json.dump(customers, fp)
    fp.close()