class Solution(object):
    def cherryPickup(self, grid):
        n = len(grid)
        m = len(grid[0])
        cache = {}
        def dfs(i, j, k):
            if (i,j,k) in cache:
                return cache[i,j,k]
            if i == n - 1:
                return grid[i][j] if j == k else grid[i][j] + grid[i][k]
            if i == n - 1:
                return grid[i][k]
            ans = 0
            for c1 in (j - 1, j, j + 1):
                for c2 in (k - 1, k, k + 1):
                    if 0 <= c1 < m and 0 <= c2 < m:
                        ans = max(ans, dfs(i + 1, c1, c2)) 
            ans += grid[i][j]
            if j != k:
                ans += grid[i][k]
            cache[i,j,k] = ans
            return ans
        return dfs(0,0,m - 1)
