import discord
import os
import requests
import random
import json
from keep_alive import keep_alive

response = requests.get("http://antiverse.trueddns.com:18527/")
client = discord.Client()


คำทักทาย = ["bobo","ว่าไง","ว่า","เออ หวัดดี","หะ","."]
เซิฟอยู่ = ["เข้าได้อยู่","ยังไม่บึ้ม","เล่นได้ ก็ออนไลน์อยู่","xenojam is still alive kuy"]
เซิฟบึ้ม = ["ไอเหี้ย พัง","ทรูกาก","เซิฟบึ้ม","เลิกทำแล้ว","xenojam is ded"]

#Random picture feature
def getSomePic():
  link = "https://picsum.photos/id/" + str(random.randint(0,1084)) + "/info"
  req = requests.get(link)
  img = json.loads(req.text)
  return img["download_url"]

@client.event
async def on_ready():
  print("KenZ is ready to serve!!!")

@client.event
async def on_message(message):
  if message.author == client.user: 
    return
  if message.content.startswith("!kenz"):
    msg = message.content.split(' ')
    if len(msg) == 1:
      await message.channel.send("command = [?, hi, hello, ถาม, xenojam, xeno]")
    else:
      command = msg[1]
    if command == "hi" or command == "hello":
      ans = random.choice(คำทักทาย)
      await message.channel.send(ans)
    elif command == "ถาม":
      await message.channel.send("ไม่รู้")
    elif command.lower() == "xenojam" or command.lower() == "xeno":
      if response.status_code == 200:
        await message.channel.send(random.choice(เซิฟอยู่))
      else:
        await message.channel.send(random.choice(เซิฟบึ้ม))
    elif command == "?":
      await message.channel.send(getSomePic())


keep_alive()
client.run(os.getenv('TOKEN'))