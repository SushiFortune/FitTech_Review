from pymongo import MongoClient

def create_database_and_insert_models():
    client = MongoClient('mongodb://localhost:27017/')

    db = client['wearable_fitness_trackers_db']

    collection = db['BestBuy FitBit model names']
    
    collection.create_index([("name", 1)], unique=True)
    
  
    popular_models = [
        {"model": "Fitbit LTE", "name": "Fitbit Ace LTE - Kids Smartwatch with In-App Calling, Messaging, GPS"},
        {"model": "Fitbit Sense 2", "name": "Fitbit - Sense 2 Advanced Health Smartwatch"},
        {"model": "Fitbit Inspire 3", "name": "Fitbit - Inspire 3 Health & Fitness Tracker"},
        {"model": "Fitbit Versa 4", "name": "Fitbit - Versa 4 Fitness Smartwatch"},
        {"model": "Fitbit Charge 6", "name": "Fitbit - Charge 6 Advanced Fitness & Health Tracker"},
        
        

    ]
    
  
    collection.insert_many(popular_models)
    
    print("Database and collection created, and documents inserted successfully.")

if __name__ == "__main__":
    create_database_and_insert_models()
