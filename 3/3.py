def find_sum(banks):
  add_up = []
  for bank in banks:
    greatest = 0
    second_greatest = 0
    for i in range(len(bank)-1):
      integer = int(bank[i])
      if integer > greatest:
        greatest = integer
        second_greatest = int(bank[-1])
      elif integer > second_greatest:
        second_greatest = integer
    add_up.append(int(str(greatest)+str(second_greatest)))
  return sum(add_up)

def find_12(banks):
  best = []
  for bank in banks:
    rank = []
    take_out = len(bank) - 12
    for i in range(len(bank)):
      while rank and int(bank[i]) > int(rank[-1]) and take_out:
        rank.pop()
        take_out -= 1
      rank.append(bank[i])
    best.append(int("".join(rank[:12])))
  return sum(best)
  

def main():
  banks = []
  with open("input.txt", "r") as f:
    for line in f:
      line = line.strip()
      banks.append(line)
  
  print(find_sum(banks))
  print(find_12(banks))


if __name__ == "__main__":
  main()