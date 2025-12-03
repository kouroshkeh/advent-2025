def find_dup(items):
  invalid = []
  for start, end in items:
    for i in range(len(str(start)), len(str(end))+1):
      if i % 2 != 0:
        continue
      
      half = i // 2

      for l in range((10**(half-1)), (10**(half))):
          check = int(str(l)+str(l))
          if  start <= check <= end:
            invalid.append(check)
  return sum(invalid)


def find_dup_gen(items):
  invalid = set()
  for start, end in items:
    for i in range(len(str(start)), len(str(end))+1):
      
      divisors = []
      j = 1
      while j * j <= i:
        if i % j == 0:
          divisors.append(j)
          if j != i // j:
            divisors.append(i//j)
        j += 1

      for k in divisors:
        if k < 2:
          continue
        half = i // k

        for l in range((10**(half-1)), (10**(half))):
            check = int(str(l)*k)
            if  start <= check <= end:
              invalid.add(check)
  return sum(invalid)

def main():
  with open("input.txt", "r") as f:
    line = f.read().strip()
  
  line = line.split(",")
  items = []

  for l in line:
    start, end = l.split("-")
    items.append([int(start), int(end)])
  
  print(find_dup(items))
  print(find_dup_gen(items))

if __name__ == "__main__":
  main()
