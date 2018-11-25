'''
    Done by: Henok Seifu
    Merchant Recommender for Customers:
        analyzes Customer portfolio and finds
        new companies matching likings in 
        portfolio.
    Dependencies: search.py
'''
import json
import search
import pandas as pd
import numpy as np

#Given a customerID, it will return a list of Merchants
#appended with the distances from customer to Merchants
def get_recom(customer_id,show=True):
    #Find customer portfolio in database
    with open("customers.json",'r') as g:
        customers = json.load(g)
        for c in customers:
            if c["id"] == customer_id:
                customer = c
                break

    #For showing customer portfolio
    if show:
        print("Customer data:")
        vals = list(customer.values())
        #Move tags into one string
        vals[3] = (' ').join(vals[3])
        keys = list(customer.keys())
        print("="*80)
        print("{:^5}{:^13}{:^40}{:<10}".format(keys[1],keys[2],keys[3],keys[0]))
        print("{:<5}{:<13}{:<40}{:^10}\n\n".format(vals[1],vals[2],vals[3],vals[0]))

    #Find matches
    ls = []
    for tag in customer["tags"]:
        for merch in search.search(tag,sortby='price_cat',show=False):
            if merch not in ls:
                ls.append(merch)
    
    #Sort closest first
    ls = sorted(ls, key=lambda k: abs(k["location"] - customer["location"]))

    #data holders
    items = []
    val3 = ["category", "name", "price_cat", "tags", "location", "id", "distance"]
    for i in ls:
        temp = []
        for key,value in i.items():
            if key == "tags":
                value = ' '.join(value)
            temp.append(value)
            temp.append(abs(customer["location"] - i["location"]))
        items.append(temp)
    items_np = np.asarray(items).transpose()
    #for showing possible merchant portfolios
    if show:
        print("="*80)
        print(pd.DataFrame(items_np,val3).transpose())
    return items
