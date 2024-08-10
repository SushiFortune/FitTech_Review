from pymongo import MongoClient

def create_database_and_insert_models():
    client = MongoClient('mongodb://localhost:27017/')

    db = client['wearable_fitness_trackers_db']

    collection = db['PCMag models XPATH']
    
    collection.create_index([("name", 1)], unique=True)
    
  
    popular_models = [
        {"name": "Fitbit Ace 3", "xpath": "/html/body/div[2]/div/main/div/header/div/div[1]/div[2]"},
        {"name": "Fitbit Luxe", "xpath": "/html/body/div[3]/div/main/div/header/div/div[1]/div[2]"},
        {"name": "Fitbit Charge 5", "xpath": "/html/body/div[3]/div/main/div/header/div/div[1]/div[2]"},
        {"name": "Fitbit Versa 3", "xpath": "/html/body/div[3]/div/main/div/header/div/div[1]/div[2]"},
        {"name": "Fitbit Sense 2", "xpath": "/html/body/div[2]/div/main/div/header/div/div[1]/div[2]"},
        
        

    ]
    
  
    collection.insert_many(popular_models)
    
    print("Database and collection created, and documents inserted successfully.")

if __name__ == "__main__":
    create_database_and_insert_models()
