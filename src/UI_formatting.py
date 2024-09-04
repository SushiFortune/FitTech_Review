import re

def format(user_input,id,type):
    user_input=user_input.lower()
    pattern = r'^[a-zA-Zíē][a-zA-Z0-9\síē]*$' 
    test=bool(re.match(pattern,user_input))
    print(test)
    if test==False:
        return None 
    

    else : 
        # Formatting for BestBuy
    

        if (id=='BestBuy' and type=='Filtering'): 

            if user_input=="garmin vivoactive 5":
                return "garmin - vívoactive 5"
            
            if user_input=="garmin vivomove trend":
                return "garmin - vívomove trend hybrid"
            
            if user_input=="garmin fenix 7s":
                return "garmin - fēnix 7s"
            
            if user_input=="garmin fenix 7x sapphire solar":
                return "garmin - fēnix 7x  sapphire solar"
            
            
            else:
                words = user_input.split()
                formatted_UI= words[0]+ " - " +' '.join(words[1:])
                return formatted_UI
    
        elif (id=='BestBuy' and type=='Fetching') :
            words=user_input.split()
            s="-"
            formatted_UI = s.join(words)
            formatted_UI
            return formatted_UI+"-smartwatch"
        
        elif (id=='PCMag' and type=='default'):
            words=user_input.split()
            s="-"
            formatted_UI = s.join(words)
            return formatted_UI
        
        
        return None
    


