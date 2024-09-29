grid = [[0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 1, 0, 0]]

m = len(grid)
n = len(grid[0])

paths = []
valid = 0

def dfs(i, j):
    path = []
    if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != 0:
        return
    else:
        path.append([i, j])
        grid[i][j] = 1
        dfs(i, j+1)
        dfs(i+1, j)
        dfs(i, j-1)
        dfs(i-1, j)
    
    paths.append(path)

for path in paths:
    if path[0] == [m-1, n-1] and path[-1] == [0, 0]:
        valid+=1

for i in range(m):
    for j in range(n):
        if grid[i][j] == 0:
            dfs(i, j)

print(valid, paths)


