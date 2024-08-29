import re


def format(user_input,id,type):
    pattern = r'^[a-zA-Zí][a-zA-Z0-9\sí]*$'
    test=bool(re.match(pattern,user_input))
    print(test)
    if test==False:
        return None 
    

    else : 
        # Formatting for BestBuy
        if id=='BestBuy' and type=='Filtering': 
           words = user_input.split()
           formatted_UI= words[0]+ " - " +' '.join(words[1:])
           return formatted_UI
        
        elif (id=='BestBuy' and type=='Fetching') :
            words=user_input.split()
            s="-"
            formatted_UI = s.join(words)
            return formatted_UI
        
        elif (id=='PCMag' and type=='default'):
            words=user_input.split()
            s="-"
            formatted_UI = s.join(words)
            return formatted_UI
        
        
        return None
    


