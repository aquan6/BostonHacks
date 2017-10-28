import json
import urllib.request as ur

def get_next_giphy(search_term):
    
    #search_term = "happy"
    API_KEY = "bv9xw5KEmBxkF8FglWO2dd9iAU0ze9Wr"
    limit = "1"
    
    
    
    
    data = json.loads(ur.urlopen("http://api.giphy.com/v1/gifs/search?q=" + search_term + "&api_key=" + API_KEY + "&limit="+limit).read())
        
    #print(json.dumps(data, sort_keys=True, indent=4))
    print(data['data'][0]['embed_url'])
    
    
#get_next_giphy()