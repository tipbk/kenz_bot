import discord
import os
from keep_alive import keep_alive
from Feature.feature_greeting import greeting
from Feature.feature_server_status import check_server_status
from Feature.feature_random_photo import random_photo
from Feature.feature_fword import fword, add_fword, rem_fword, list_fword
from Feature.feature_tu_photo import add_tu, rem_tu, list_tu, tu
from Feature.feature_roll import roll
from Feature.feature_show_command import show_command
from Feature.feature_get_crypto_data import get_crypto_data
from Feature.feature_gacha import gacha
from Feature.feature_ask import ask

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
      await message.channel.send(ask())
    elif command.lower() == "xenojam" or command.lower() == "xeno" or command.lower() == "server":
      await message.channel.send(check_server_status())
    elif command == "?":
      await message.channel.send(random_photo())
    elif command == "roll":
      await message.channel.send(roll())
    elif command == "ด่า":
      await message.channel.send(fword(msg))
    elif command == "เพิ่มคำด่า":
      await message.channel.send(add_fword(msg))
    elif command == "ลบคำด่า":
      await message.channel.send(rem_fword(msg))
    elif command == "คำด่า":
      await message.channel.send(list_fword())
    elif command == "ตู่":
      await message.channel.send(tu())
    elif command == "เพิ่มรูปตู่":
      await message.channel.send(add_tu(msg))
    elif command == "ลบรูปตู่":
      await message.channel.send(rem_tu(msg))
    elif command == "รูปตู่":
      await message.channel.send(list_tu())
    elif command == "coin":
      await message.channel.send(get_crypto_data(msg))
    elif command == "gacha":
      await message.channel.send(gacha(msg))
    elif command == "ระเบิดเวลา":
      await message.channel.send("อ๊าาาาาาาาาาาาาาาาาาาาาาาาาาาาาาาาาาาาาาา")

keep_alive()
client.run(os.getenv('TOKEN'))
