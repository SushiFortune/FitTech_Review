import bestbuy_fitbit_data_collection
import bestbuy_garmin_data_collection

def choice(user_input):
    user_input=user_input.lower()

    if "garmin" in user_input:
        return bestbuy_garmin_data_collection.get_rating(user_input)
    
    elif "fitbit" in user_input:
        return bestbuy_fitbit_data_collection.get_rating(user_input)
    
    else:
        return None