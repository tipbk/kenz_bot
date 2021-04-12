from random import choice
import socket

เซิฟอยู่ = ["เข้าได้อยู่","ยังไม่บึ้ม","เล่นได้ ก็ออนไลน์อยู่","xenojam is still alive kuy"]
เซิฟบึ้ม = ["ไอเหี้ย พัง","ทรูกาก","เซิฟบึ้ม","เลิกทำแล้ว","xenojam is ded"]

def check_server_status():
  s = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)
  try:
      s.connect(("antiverse.trueddns.com", 18526))
      return choice(เซิฟอยู่)
  except:
      return choice(เซิฟบึ้ม)
