class Solution:
	# 递归+记忆化
    def calculateMinimumHP(self, dungeon):
        if not dungeon or not len(dungeon[0]):
            return 0
        n = len(dungeon)
        m = len(dungeon[0])
        d = dict()
        def dfs(i,j):
            if (i,j) in d:
                return d[i,j]
            if i>=n or j>=m:
                return float("inf")
            if i==n-1 and j==m-1:
                return 0 if dungeon[i][j]>=0 else abs(dungeon[i][j])
            right = dfs(i,j+1)
            down = dfs(i+1,j)
            res = min(right,down) - dungeon[i][j]
            d[i,j] = res if res>=0 else 0
            return d[i,j]
        return dfs(0,0)+1
		
		
		
	# 动态规划，二维数组
    def calculateMinimumHP(self, dungeon):
        if not dungeon or not len(dungeon[0]):
            return 0
        n = len(dungeon)
        m = len(dungeon[0])
        dp = [[float("inf") for _ in xrange(m+1)] for _ in xrange(n+1) ]
        dp[n][m-1] = 0
        dp[n-1][m] = 0
        for i in xrange(n-1,-1,-1):
            for j in xrange(m-1,-1,-1):
                dp[i][j] = max( min(dp[i+1][j],dp[i][j+1])-dungeon[i][j], 0 )
        return dp[0][0]+1
		
		
		
	# 另一种好理解一些的dp，二维数组
    def calculateMinimumHP(self, dungeon):
        if not dungeon or not dungeon[0]:
            return 0
        n = len(dungeon)
        m = len(dungeon[0])
        dp = [[0 for _ in xrange(m)] for _ in xrange(n)]
        dp[-1][-1] = 0 if dungeon[-1][-1]>=0 else abs(dungeon[-1][-1])
        for i in xrange(n-2,-1,-1):
            dp[i][m-1] = max(dp[i+1][m-1]-dungeon[i][m-1],0)
        for j in xrange(m-2,-1,-1):
            dp[n-1][j] = max(dp[n-1][j+1]-dungeon[n-1][j],0)
        for i in xrange(n-2,-1,-1):
            for j in xrange(m-2,-1,-1):
                right = max(dp[i][j+1]-dungeon[i][j],0)
                down = max(dp[i+1][j]-dungeon[i][j],0)
                dp[i][j] = min(right,down)
        return dp[0][0]+1
		
		
		
	# 动态规划，一维数组
    def calculateMinimumHP(self, dungeon):
        if not dungeon or not dungeon[0]:
            return 0
        n = len(dungeon)
        m = len(dungeon[0])
        dp = [0]*(m+1)
        for i in xrange(m-1,-1,-1):
            dp[i] = max(dp[i+1]-dungeon[-1][i],0)
        dp[-1] = float("inf")
        for i in xrange(n-2,-1,-1):
            for j in xrange(m-1,-1,-1):
                dp[j] = max( min(dp[j],dp[j+1])-dungeon[i][j], 0 )
        return dp[0]+1
		