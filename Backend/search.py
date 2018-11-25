'''
    Done by: Henok Seifu
    Merchant finder for Customers matching
    their portfolio.
'''

import json
import pandas as pd
import numpy as np

#Given a specific tag, return merchants having such tags
def search(tag, sortby="price_cat",show=False):
    #Read and filter merchants
    with open("merchants.json",'r') as f:
        val1 = json.load(f)
        val2 = []
        for merch in val1:
            if tag in merch["tags"]:
                val2.append(merch)
    
    #Sort according to parameter provided
    val2 = sorted(val2, key=lambda k: k[sortby])

    #Data holders
    items = []
    val3 = ["category", "name", "tags", "price_cat", "location", "id"]
    for i in val2:
        temp = []
        for key,value in i.items():
            if key == "tags":
                value = ' '.join(value)
            temp.append(value)
        items.append(temp)
    items = np.asarray(items).transpose()

    #Showing search results
    if show:
        print("Search results:")
        print(pd.DataFrame(items,val3).transpose())
    return val2