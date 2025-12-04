def solve(grid):
  counter = 0
  directions = [(0,1),(1,0),(-1,0),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      if grid[i][j] != "@":
        continue
      limit = 0
      for d in directions:
        x,y = i+d[0], j+d[1]
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
          if grid[x][y] == "@":
            limit += 1
      if limit < 4:
        counter += 1
  return counter

def change(grid):
  counter = 0
  track = []
  directions = [(0,1),(1,0),(-1,0),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      if grid[i][j] != "@":
        continue
      limit = 0
      for d in directions:
        x,y = i+d[0], j+d[1]
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
          if grid[x][y] == "@":
            limit += 1
      if limit < 4:
        track.append((i,j))
        counter += 1
  for t in track:
    grid[t[0]][t[1]] = "."
  return grid, counter

def solve_2(grid):
  mut = [list(g) for g in grid]
  grid, counter = change(mut)
  total = counter
  while counter:
    newgrid, counter = change(grid)
    total += counter
    grid = newgrid

  return total

def main():
  grid = []
  with open("input.txt", "r") as f:
    for line in f:
      line = line.strip()
      grid.append(line)
  print(solve(grid))
  print(solve_2(grid))

if __name__ == "__main__":
  main()