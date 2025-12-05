def merge_solve(ranges, vals):
  ranges.sort(key= lambda x: (x[0],x[1]))
  stack = []
  for r in ranges:
    if stack and stack[-1][1] >= r[0]:
      best = [min(r[0],stack[-1][0]), max(r[1],stack[-1][1])]
      stack[-1] = best
    else:
      stack.append(r)
  
  counter = 0
  for val in vals:
    for s in stack:
      if s[0] <= val <= s[1]:
        counter += 1
        break
  
  return counter, sum([(s[1]-s[0])+1 for s in stack])

def main():
  ranges = []
  with open("input.txt", "r") as f:
    range_part, vals_part = f.read().strip().split("\n\n")

    for r in range_part.splitlines():
        first, second = r.split("-")
        ranges.append([int(first),int(second)])

    vals = [int(v) for v in vals_part.splitlines()]
  print(merge_solve(ranges, vals))

if __name__ == "__main__":
  main()