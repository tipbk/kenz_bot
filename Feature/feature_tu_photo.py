from random import choice
from replit import db

value = db["รูปภาพ"]

def add_tu(msg):
  global value

  if msg[2] in value:
    return "รูปนี้มีแล้ว " + msg[2]
  else:
    value.append(msg[2])
    db["รูปภาพ"] = value
    value = db["รูปภาพ"]
    return msg[2] + " ถูกเพิ่มเรียบร้อยแล้ว"

def rem_tu(msg):
  global value

  if not msg[2] in value:
    return "รูป " + msg[2] + " ไม่มี "
  else:
    value.remove(msg[2])
    db["รูปภาพ"] = value
    value = db["รูปภาพ"]
    return msg[2] + " ถูกลบละ"

def tu():
  return choice(value)

def list_tu():
  global value
  photo_list = '```'
  for i, item in enumerate(value,1):
      photo_list += (str(i) + '. ' + item + '\n')
  photo_list = photo_list + '```'
  return photo_list
