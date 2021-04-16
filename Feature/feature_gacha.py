import random

def gacha(msg):
  if len(msg) == 2:
    return "ใส่เปอร์เซ็นต์มาด้วย"
  else:
    if msg[2][-1] == "%":
      msg[2] = msg[2][:-1]
    return cal_chance(float(msg[2]))
  
def cal_chance(number):
  random_number = random.uniform(0,100)
  if number > 100 or number < 0:
    return "เอาดีๆ ขอไม่เกิน 100 และไม่น้อยกว่า 0"
  elif random_number < number:
    return "ไม่เกลือโว้ย"
  else:
    return "เกลือ"
