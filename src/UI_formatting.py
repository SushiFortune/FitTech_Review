import re
from pymongo import MongoClient

def format(user_input,id):
    pattern = r'^[a-zA-Z][a-zA-Z0-9\s]*$'
    test=bool(re.match(pattern,user_input))
    if test==False:
        return None 
    

    else : 
        # Formatting for BestBuy
        if id==0: 
            formatted_UI = get_name_by_model(user_input)
            return formatted_UI

        # Formatting for PCMag
        elif id==1:
            words=user_input.split()
            s="-"
            formatted_UI = s.join(words)
            return formatted_UI
        
        
        return None
    

def get_name_by_model(model_value):

    client = MongoClient('mongodb://localhost:27017/')
    db = client['wearable_fitness_trackers_db']
    collection = db['BestBuy FitBit model names']

    document = collection.find_one({"model": model_value})
    if document:
        return document.get("name")
    else:
        return None