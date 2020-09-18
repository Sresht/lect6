import requests
import os
import json
from os.path import join, dirname
from dotenv import load_dotenv
import json

dotenv_path = join(dirname(__file__), 'spoonacular.env')
load_dotenv(dotenv_path)

spoonacular_key = os.environ['SPOONACULAR_KEY']
url = "https://api.spoonacular.com/recipes/search?apiKey={}".format(spoonacular_key)

response = requests.get(url)
json_body = response.json()
<<<<<<< HEAD
print(json.dumps(json_body))
=======
print(json.dumps(json_body["results"][0]["readyInMinutes"], indent=2))
>>>>>>> 9e7a95be9cbbe7ec53e506c33c479eca182c6ce1
