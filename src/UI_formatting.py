import re
def format(user_input,id):
    pattern = r'^[a-zA-Z0-9\s]+$'
    test=bool(re.match(pattern,user_input))
    # user_input = user_input.strip().lower()
    # words=user_input.split()
    if test==False:
        return None 
    

    else : 
        words=user_input.split()

        # Formatting for BestBuy 
        if id==0: 
            # if " - " in user_input:
            #     parts = user_input.split(" - ")
            #     if len(parts) == 2 and all(parts):
            #         return user_input
        
            # words = user_input.split()
            # if len(words) > 1 and "-" not in user_input:
            formatted_UI = words[0] + " - " + " ".join(words[1:])
            return formatted_UI
            
            # return None

        # Formatting for PCMag
        elif id==1:

            # words = user_input.split()
            s="-"
            # if len(words) > 1 and "-" not in user_input:
            formatted_UI = s.join(words)
            return formatted_UI
        
        
        return None
