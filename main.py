import discord
import os
import requests
import random


response = requests.get("http://antiverse.trueddns.com:18527/")
client = discord.Client()

คำทักทาย = ["bobo","ว่าไง","ว่า","เออ หวัดดี","หะ","."]
เซิฟอยู่ = ["เข้าได้อยู่","ยังไม่บึ้ม","เล่นได้ ก็ออนไลน์อยู่","xenojam is still alive kuy"]
เซิฟบึ้ม = ["ไอเหี้ย พัง","ทรูกาก","เซิฟบึ้ม","เลิกทำแล้ว","xenojam is ded"]

@client.event
async def on_ready():
  print("Hello")

@client.event
async def on_message(message):
  if message.author == client.user: 
    return
  if message.content.startswith("$kenz"):
    msg = message.content.split(' ')
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

client.run(os.getenv('TOKEN'))