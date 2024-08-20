from pymongo import MongoClient

def create_database_and_insert_models():
    client = MongoClient('mongodb://localhost:27017/')

    db = client['wearable_fitness_trackers_db']

    FitBit_collection = db['BestBuy FitBit model names']
    
    FitBit_collection.create_index([("name", 1)], unique=True)
    
    popular_fitbit_models = [
        {"model": "fitbit lte", "name": "Fitbit Ace LTE - Kids Smartwatch with In-App Calling, Messaging, GPS"},
        {"model": "fitbit sense 2", "name": "Fitbit - Sense 2 Advanced Health Smartwatch"},
        {"model": "fitbit inspire 3", "name": "Fitbit - Inspire 3 Health & Fitness Tracker"},
        {"model": "fitbit versa 4", "name": "Fitbit - Versa 4 Fitness Smartwatch"},
        {"model": "fitbit charge 6", "name": "Fitbit - Charge 6 Advanced Fitness & Health Tracker"},

    ]

    FitBit_collection.insert_many(popular_fitbit_models)

    Garmin_collection = db['BestBuy Garmin model names']
    
    Garmin_collection.create_index([("name", 1)], unique=True)
    
    popular_garmin_models = [
        {"model": "Garmin Epix Pro", "name": "garmin-epix-pro-gen-2-sapphire-edition-51mm-fiber-reinforced-polymer"},
        {"model": "Garmin instinct 2X solar", "name": "garmin-instinct-2x-solar-smartwatch-50-mm-fiber-reinforced-polymer"},
        {"model": "Garmin Vivoactive 5", "name": "garmin-vivoactive-5-gps-smartwatch-42-mm-fiber-reinforced-polymer"},
        {"model": "Garmin forerunner 965", "name": "garmin-forerunner-965-gps-smartwatch-47-mm-fiber-reinforced-polymer"},
        {"model": "Garmin forerunner 265", "name": "garmin-forerunner-265-gps-smartwatch-46-mm-fiber-reinforced-polymer"},
        {"model": "Garmin Fenix 7 Pro", "name": "garmin-fenix-7-pro-sapphire-solar-gps-smartwatch-47-mm-fiber-reinforced-polymer"},
        {"model": "Garmin Fenix 7x", "name": "garmin-instinct-2x-solar-smartwatch-50-mm-fiber-reinforced-polymer"},
        {"model": "Garmin Vivoactive 5", "name": "garmin-vivoactive-5-gps-smartwatch-42-mm-fiber-reinforced-polymer"},
        {"model": "Garmin forerunner 965", "name": "garmin-forerunner-965-gps-smartwatch-47-mm-fiber-reinforced-polymer"},
        {"model": "Garmin forerunner 265", "name": "garmin-forerunner-265-gps-smartwatch-46-mm-fiber-reinforced-polymer"},

    ]

    Garmin_collection.insert_many(popular_garmin_models)
    print("Database and collection created, and documents inserted successfully.")

if __name__ == "__main__":
    create_database_and_insert_models()
