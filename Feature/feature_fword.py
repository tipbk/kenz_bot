from random import choice
from replit import db

value = db["คำด่า"]

def add_fword(msg):
  global value

  if msg[2] in value:
    return "คำว่า " + msg[2] + " ซ้ำ " + choice(value)
  else:
    value.append(msg[2])
    db["คำด่า"] = value
    return msg[2] + " ถูกเพิ่มเรียบร้อยแล้ว"

def rem_fword(msg):
  global value

  if not msg[2] in value:
    return "คำว่า " + msg[2] + " ไม่มี " + choice(value)
  else:
    value.remove(msg[2])
    db["คำด่า"] = value
    return msg[2] + " ถูกลบละ"

def fword(msg):
  if len(msg) == 2:
    return f_command()
  else:
    new_str = " ".join([ms for ms in msg[2:]])
    return new_str + " " + f_command()
  
def f_command():
  return choice(value)

def list_fword():
  global value
  word_list = '```'
  for i, item in enumerate(value,1):
      word_list+=(str(i) + '. ' + item + '\n')
  word_list = word_list + '```'
  return word_list
