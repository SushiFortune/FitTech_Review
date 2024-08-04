from pymongo import MongoClient

def create_database_and_insert_models():
    client = MongoClient('mongodb://localhost:27017/')

    db = client['wearable_fitness_trackers_db']

    collection = db['popular_models']
    
    collection.create_index([("name", 1)], unique=True)
    
  
    popular_models = [
        {"name": "Fitbit Charge 6"},
        {"name": "Fitbit Versa 4"},
        {"name": "Fitbit Sense 2"},
        {"name": "Fitbit Inspire 3"},
        {"name": "Fitbit Ace"}
    ]
    
  
    collection.insert_many(popular_models)
    
    print("Database and collection created, and documents inserted successfully.")

if __name__ == "__main__":
    create_database_and_insert_models()
