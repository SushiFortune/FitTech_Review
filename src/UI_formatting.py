import re


def format(user_input,id):
    pattern = r'^[a-zA-Z][a-zA-Z0-9\s]*$'
    test=bool(re.match(pattern,user_input))
    if test==False:
        return None 
    

    else : 
        # Formatting for BestBuy
        if id=='BestBuy': 
            formatted_UI = user_input
            return formatted_UI

        # Formatting for PCMag
        elif id=='PCMag':
            words=user_input.split()
            s="-"
            formatted_UI = s.join(words)
            return formatted_UI
        
        
        return None
    


