n = 20
m = 20

grid = [[0] * n] * m

for i, j in zip(range(m), range(n)):
    grid[i][n-1] = 1
    grid[m-1][j] = 1

for i in range(m-1,0,-1):
    for j in range (n-1,0,-1):
        grid[i][j] = grid[i][j] +  grid[i][j]


print(sum(sum(x) for x in grid))
