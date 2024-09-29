# If 1 is encountered convert that and all neighbouring to 0 -> increment num by 1

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        m, n = len(grid), len(grid[0])
        num = 0

        def dfs(i, j):
            if i<0 or i>=m or j<0 or j>=n or grid[i][j] != '1':
                return
            else:
                grid[i][j] = '0'
                dfs(i, j+1)
                dfs(i+1, j)
                dfs(i, j-1)
                dfs(i-1, j)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    num += 1
                    dfs(i, j)

        return num