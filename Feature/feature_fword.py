from random import choice

คำด่า = ["ไอควาย","หน้าหี","ลูกกะหรี่","โง่จังวะ","bobo","อ่อน","ตัวๆป่าวสาดดด","สมองมีป่าว","กระจอกว่ะ","ไม่จ๊าบเลย","ขอให้ตายไปอยู่กับลุงตู่","ไอเหี้ย"]

def fword(msg):
  
  if len(msg) == 2:
    return f_command()
  else:
    new_str = " ".join([ms for ms in msg[2:]])
    return new_str + " " + f_command()
  

def f_command():
  return choice(คำด่า)
