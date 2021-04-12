import json
from random import randint
import requests

def random_photo():
  link = "https://picsum.photos/id/" + str(randint(0,1084)) + "/info"
  req = requests.get(link)
  img = json.loads(req.text)
  return img["download_url"]
