import re
def format(user_input,id):
    pattern = r'^[a-zA-Z][a-zA-Z0-9\s]*$'
    test=bool(re.match(pattern,user_input))
    if test==False:
        return None 
    

    else : 

        words=user_input.split()

        # Formatting for BestBuy
        if id==0: 
            formatted_UI = words[0] + " - " + " ".join(words[1:])
            return formatted_UI

        # Formatting for PCMag
        elif id==1:
            s="-"
            formatted_UI = s.join(words)
            return formatted_UI
        
        
        return None
