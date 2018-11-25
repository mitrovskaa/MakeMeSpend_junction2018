import entity_analysis
import json

def get_tags(text,merchant_id,customer_id):
    entites = entity_analysis.entities_text(text)
    entity_type = ("clothes","food","drinks","entertainment")
    tags = []
    count = 0
    for entity in entites:
        if entity.name not in entity_type and entity.salience >= 0.5:
            tags.append(entity.name)
            count +=1
        if count == 5:
            break

    f = open("merchants.json",'r')
    data = json.load(f)
    
    for merchant in data:
        if merchant["id"] == merchant_id:
            print("Old tags for merchants ",merchant_id)
            for tag in merchant["tags"]:
                print('- ' + tag)

            merchant["tags"] += tags
            merchant["tags"] = list(set(merchant["tags"]))
            print("New tags for merchant ",merchant_id)
            for tag in merchant["tags"]:
                print('- ' + tag)

            print("Added ")
            for new in tags:
                print(new)
            print("\nFrom review: ")
            print(text)
            break
    f.close()
    f = open("merchants.json",'w')
    json.dump(data,f)
    f.close()
    
    c = open("customers.json",'r')
    data = json.load(c)
    for customer in data:
        if customer["id"] == customer_id:
            
            customer["tags"] += tags
            customer["tags"] = list(set(customer["tags"]))
           
            break
    c.close()
    
    c = open("customers.json",'w')
    
    json.dump(data,c)
    c.close()