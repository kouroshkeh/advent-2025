import math

def do_calulation(columns, operators):
    total = 0
    for i in range(len(columns)):
        if operators[i] == "*":
            total += math.prod(columns[i])
        else:
            total += sum(columns[i])
    return total

def do_weird_cal(columns, operators):
  return 


def main():
    rows = []
    with open("input.txt", "r") as f:
        for line in f:
            rows.append(line.rstrip("\n"))

    operators_line = rows.pop()
    longest = max(len(r) for r in rows + [operators_line])
    rows = [r.ljust(longest) for r in rows]
    operators_line = operators_line.ljust(longest)

    map_of_empty = [1] * longest
    for r in rows:
        for i, ch in enumerate(r):
            if ch != " ":
                map_of_empty[i] = 0

    breaks = {i for i, m in enumerate(map_of_empty) if m == 1}

    blocks = []
    in_block = False
    start = None
    for i in range(longest):
        if i in breaks:
            if in_block:
                blocks.append((start, i - 1))
                in_block = False
                start = None
        else:
            if not in_block:
                in_block = True
                start = i
    if in_block:
        blocks.append((start, longest - 1))

    cols = []
    ops = []

    for start, end in blocks:
        nums = []
        for r in rows:
            s = r[start:end+1].strip()
            if s:
                nums.append(int(s))
        cols.append(nums)

        op_char = None
        for i in range(start, end + 1):
            ch = operators_line[i]
            if ch in "+*":
                op_char = ch
                break
        ops.append(op_char)

    cols_part2 = []
    for start, end in blocks:
      nums = []
      for c in range(end, start - 1, -1):
          s = ""
          for r in rows:
              ch = r[c]
              if ch.isdigit():
                  s += ch
          if s:
              nums.append(int(s))
      cols_part2.append(nums)

    print(do_calulation(cols, ops))
    print(do_calulation(cols_part2, ops))

if __name__ == "__main__":
    main()