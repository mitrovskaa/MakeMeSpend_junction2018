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

    keys = list(customer.keys())
    vals = list(customer.values())
    id_index,name_index,tags_index,location_index,count = 0,0,0,0,0
    for i in keys:
        if i == 'tags':
            tags_index = count
        elif i == 'location':
            location_index = count
        elif i == 'name':
            name_index = count
        elif i == 'id':
            id_index = count 
        count+=1
    #For showing customer portfolio
    if show:
        print("Customer data:")
        
        #Move tags into one string
        vals[tags_index] = (' ').join(vals[tags_index])
        
        print("="*80)
        print("{:^5}{:^13}{:^40}{:<10}".format(keys[id_index],keys[name_index],keys[tags_index],keys[location_index]))
        print("{:<5}{:<13}{:<40}{:^10}\n\n".format(vals[id_index],vals[name_index],vals[tags_index],vals[location_index]))

    #Find matches
    ls = []
    for tag in customer["tags"]:
        for merch in search.search(tag):
            if merch not in ls:
                ls.append(merch)
    
    #Sort closest first
    ls = sorted(ls, key=lambda k: abs(k["location"] - customer["location"]))

    #data holders
    items = []
    val3 = ["category", "name", "price_cat", "tags", "location", "id"]
    for i in ls:
        temp = []
        for key,value in i.items():
            if key == "tags":
                value = ' '.join(value)
            temp.append(value)
        items.append(temp)
    items_np = np.asarray(items).transpose()
    #for showing possible merchant portfolios
    if show:
        print("="*80)
        print(pd.DataFrame(items_np,val3).transpose())
    return items
