
def format(user_input):
    user_input = user_input.strip().lower()

    if " - " in user_input:
        parts = user_input.split(" - ")
        if len(parts) == 2 and all(parts):
            return user_input
  
    words = user_input.split()
    if len(words) > 1 and "-" not in user_input:
        formatted_UI = words[0] + " - " + " ".join(words[1:])
        return formatted_UI
    
    return None
