class Solution(object):
    def minFallingPathSum(self, grid):
        n = len(grid)
        dp = [[float("inf") for _ in range(n)] for _ in range(n)]
        min_1,min_2 = -1,-1
        for j in range(n):
            dp[0][j] = grid[0][j]
            if grid[0][j] < (float("inf") if min_1 == -1 else dp[0][min_1]):
                min_2 = min_1
                min_1 = j
            elif grid[0][j] < (float("inf") if min_2 == -1 else dp[0][min_2]):
                min_2 = j
        for i in range(1, n):
            t1,t2 = -1,-1
            for j in range(n):
                if j != min_1:
                    dp[i][j] = dp[i - 1][min_1] + grid[i][j]
                else:
                    dp[i][j] = dp[i - 1][min_2] + grid[i][j]
                if dp[i][j] < (float("inf") if t1 == -1 else dp[i][t1]):
                    t2 = t1
                    t1 = j
                elif dp[i][j] < (float("inf") if t2 == -1 else dp[i][t2]):
                    t2 = j
                    
            min_1 = t1
            min_2 = t2
        return min(dp[-1])
		
	

	# dfs 实现，代码很精简，但是会超时
class Solution(object):
    def minFallingPathSum(self, grid):
        n = len(grid)
        @lru_cache
        def dfs(i, j):
            if i == n or j < 0 or j >= n:
                return float("inf")
            tmp = float("inf")
            for k in range(n):
                if k != j:
                    tmp = min(tmp, dfs(i + 1, k) + grid[i][j])
            return tmp if tmp != float("inf") else grid[i][j]
        return min(dfs(0,j) for j in range(n))