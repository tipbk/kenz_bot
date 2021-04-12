import discord
import os
import requests
import random
import json
import socket
from keep_alive import keep_alive


client = discord.Client()

#List of words that we gonna use
คำทักทาย = ["bobo","ว่าไง","ว่า","เออ หวัดดี","หะ","."]
เซิฟอยู่ = ["เข้าได้อยู่","ยังไม่บึ้ม","เล่นได้ ก็ออนไลน์อยู่","xenojam is still alive kuy"]
เซิฟบึ้ม = ["ไอเหี้ย พัง","ทรูกาก","เซิฟบึ้ม","เลิกทำแล้ว","xenojam is ded"]

#Random picture feature
def get_some_pic():
  link = "https://picsum.photos/id/" + str(random.randint(0,1084)) + "/info"
  req = requests.get(link)
  img = json.loads(req.text)
  return img["download_url"]

def check_server_status():
  s = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)
  try:
      s.connect(("antiverse.trueddns.com", 18526))
      return random.choice(เซิฟอยู่)
  except:
      return random.choice(เซิฟบึ้ม)



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
      await message.channel.send('''
      Command List:
      ? = send a random picture
      hi, hello = KenZ will reply you with random greeting words
      ถาม = He will answer "ไม่รู้"
      roll = KenZ will roll a number from 0 - 100
      xenojam, xeno, server = to check xenojam server status
                                    ''')
    else:
      command = msg[1]
    if command == "hi" or command == "hello":
      await message.channel.send(random.choice(คำทักทาย))
    elif command == "ถาม":
      await message.channel.send("ไม่รู้")
    elif command.lower() == "xenojam" or command.lower() == "xeno" or command.lower() == "server":
      await message.channel.send(check_server_status())
    elif command == "?":
      await message.channel.send(get_some_pic())
    elif command == "roll":
      await message.channel.send("ได้เลข " + str(random.randint(0,100))+ " จ่ะ")


keep_alive()
client.run(os.getenv('TOKEN'))
