import requests
import json

endpoint = "https://api.bitkub.com/api/market/ticker?sym="

def check_coin(coin):
  params = "THB_" + coin.upper()
  try:
    req = requests.get(endpoint + params)
    data = json.loads(req.text)
    return "ราคา " + coin.upper() + " ตอนนี้คือ " + str(data[params]["last"]) + " บาท"
  except:
    return "เหรียญอะไร มั่วล่ะๆ"

def get_crypto_data(msg):
  if len(msg) == 2:
    return "ใส่ชื่อเหรียญมาด้วยยย"
  else:
    return check_coin(msg[2])