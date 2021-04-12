import discord
import os
from keep_alive import keep_alive
from Feature.feature_greeting import greeting
from Feature.feature_server_status import check_server_status
from Feature.feature_random_photo import random_photo
from Feature.feature_fword import fword
from Feature.feature_roll import roll
from Feature.feature_show_command import show_command
from Feature.feature_get_crypto_data import get_crypto_data

client = discord.Client()

@client.event
async def on_ready():
  print("KenZ is ready to serve!!!")

@client.event
async def on_message(message):
  if message.author == client.user: 
    return
  command = ""
  if message.content.startswith("!kenz"):
    msg = message.content.split(' ')
    if len(msg) == 1:
      await message.channel.send(show_command())
    else:
      command = msg[1]
    if command == "hi" or command == "hello":
      await message.channel.send(greeting())
    elif command == "ถาม":
      await message.channel.send("ไม่รู้")
    elif command.lower() == "xenojam" or command.lower() == "xeno" or command.lower() == "server":
      await message.channel.send(check_server_status())
    elif command == "?":
      await message.channel.send(random_photo())
    elif command == "roll":
      await message.channel.send(roll())
    elif command == "ด่า":
      if len(msg) == 2:
        await message.channel.send(fword())
      else:
        await message.channel.send(msg[2] + " " + fword())
    elif command == "price":
      if len(msg) == 2:
        await message.channel.send("ใส่ชื่อเหรียญมาด้วยยย")
      else:
        await message.channel.send(get_crypto_data(msg[2]))


keep_alive()
client.run(os.getenv('TOKEN'))
