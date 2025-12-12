def do_bfs(grid, start):
  deque = [start]
  wood_total = 0
  for i in range(len(grid)):
    temp = set()
    while deque:
      node = deque.pop()
      if grid[i][node] == "." or grid[i][node] == "S":
        temp.add(node)
      else:
        wood_total += 1
        if node - 1 >= 0:
          temp.add(node-1)
        if node + 1 < len(grid[0]):
          temp.add(node+1)
    deque.extend(temp)
  return wood_total


# this timed out for part2, input is too big
def do_dfs(grid, start):
  total = 0
  def dfs(node, row):
    nonlocal total
    if row >= len(grid):
      total += 1
      return 
    next_nodes = []
    if grid[row][node] == "S" or grid[row][node] == ".":
      next_nodes.append(node)
    else:
      if node - 1 >= 0:
        next_nodes.append(node-1)
      if node + 1 < len(grid[0]):
        next_nodes.append(node+1)
    for n in next_nodes:
      dfs(n, row+1)
  dfs(start, 0)
  return total

def do_dp(grid, start):
  num_ways = [0] * len(grid[0])
  num_ways[start] = 1
  for i in range(len(grid)):
    ways = [0] * len(grid[0])
    for j, prev in enumerate(num_ways):
      if grid[i][j] == "S" or grid[i][j] == ".":
        ways[j] += prev
      else: 
        if j - 1 >= 0:
          ways[j-1] += prev
        if j + 1 < len(grid[0]):
          ways[j+1] += prev
    num_ways = ways
  return sum(num_ways)
    


def main():
  with open("input.txt", "r") as f:
    grid = []
    for line in f:
      row = []
      for char in line.strip():
        row.append(char)
      grid.append(row)

  start = None
  for i in range(len(grid[0])):
    if grid[0][i] == "S":
      start = i
  print(do_bfs(grid, start))
  print(do_dp(grid, start))


if __name__ == "__main__":
  main()