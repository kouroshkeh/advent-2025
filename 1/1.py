def calculate(items):
  current = 0
  start = 50
  for item in items:
    direction, value = item[0], item[1]
    step = -1 if direction == "L" else 1

    start = (start + step*value) % 100
    if start == 0:
      current += 1
  return current

def calculat_with_rot(items):
  current = 0
  start = 50
  for item in items:
    direction, value = item[0], item[1]
    step = -1 if direction == "L" else 1

    toadd = 0
    temp = start
    if step == -1:
      if temp == 0:
        temp -= value
        toadd += abs(temp) // 100
      else:
        temp -= value
        if temp <= 0:
          toadd += (1 + abs(temp) // 100)
    else:
      temp += value 
      toadd += temp // 100
     
    current += toadd
    start = (start + step*value) % 100


    
  return current

  
def main():
  items = []
  with open("input.txt", "r") as f:
    for line in f:
      line = line.strip()
      direction = line[0]
      value = int(line[1:])
      items.append([direction, value])
  
  print(calculate(items))
  print(calculat_with_rot(items))

if __name__ == "__main__":
  main()



    