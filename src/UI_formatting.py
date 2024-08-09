
def format(user_input,id):
    user_input = user_input.strip().lower()
    
    if id==0:
        if " - " in user_input:
            parts = user_input.split(" - ")
            if len(parts) == 2 and all(parts):
                return user_input
    
        words = user_input.split()
        if len(words) > 1 and "-" not in user_input:
            formatted_UI = words[0] + " - " + " ".join(words[1:])
            return formatted_UI
        
        return None
    
    elif id==1:

        words = user_input.split()
        s="-"
        if len(words) > 1 and "-" not in user_input:
            formatted_UI = s.join(words)
        return formatted_UI
    
    
    return None
