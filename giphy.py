import json
import urllib.request as ur
import random as random

def get_next_giphy(x, y):
    
    good_threshold = 40
    bad_threshold = 20
    
    API_KEY = "bv9xw5KEmBxkF8FglWO2dd9iAU0ze9Wr"
    limit = "1"
    offset = str(random.randrange(25))
    avg = (x+y)/2
    
    
    if avg<=bad_threshold:
        search_term = "bad"
        
    elif avg>bad_threshold and avg<good_threshold:
        search_term = "not+bad"
        
    else:
        search_term = "awesome"
        
    data = json.loads(ur.urlopen("http://api.giphy.com/v1/gifs/search?q=" + search_term + "&api_key=" + API_KEY + "&limit="+limit + "&offset=" + offset).read())
    
    print(data['data'][0]['embed_url'])
    

get_next_giphy(50, 50)