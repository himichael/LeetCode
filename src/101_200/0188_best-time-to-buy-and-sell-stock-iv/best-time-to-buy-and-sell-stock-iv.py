class Solution(object):
	
	# 递归+记忆化，k超大时做优化，退换为无限次买卖
	def maxProfit(self, k, prices):
		"""
		:type k: int
		:type prices: List[int]
		:rtype: int
		"""
		if not prices or k<=0:
			return 0
		n = len(prices)
		if k>n/2:
			dp = [[0 for _ in xrange(2)] for _ in xrange(n)]
			dp[0][0] = 0
			dp[0][1] = -prices[0]
			for i in xrange(1,n):
				dp[i][0] = max(dp[i-1][0],dp[i-1][1]+prices[i])
				dp[i][1] = max(dp[i-1][1],dp[i-1][0]-prices[i])
			return max(dp[n-1][0],0)	
		mem = [[[-1 for _ in xrange(2)] for _ in xrange(k+1)] for _ in xrange(n)]	
		def dfs(index,count,status):
			if index==n or (count==k and status==0):
				return 0
			if mem[index][count][status]>-1:
				return mem[index][count][status]
			a = dfs(index+1,count,status)
			b,c = 0,0
			if status:
				b = dfs(index+1,count,0)+prices[index]
			else:
				c = dfs(index+1,count+1,1)-prices[index]
			mem[index][count][status] = max(a,b,c)
			return mem[index][count][status]
		return dfs(0,0,0)
		
		
		
		
	# 递归(超时)	
	def maxProfit(self, k, prices):
		"""
		:type k: int
		:type prices: List[int]
		:rtype: int
		"""
		if not prices:
			return 0
		n = len(prices)
		def dfs(index,count,status):
			if index==n or (count==k and status==0):
				return 0
			a = dfs(index+1,count,status)
			b,c = 0,0
			if status:
				b = dfs(index+1,count,0)+prices[index]
			else:
				c = dfs(index+1,count+1,1)-prices[index]
			return max(a,b,c)
		return dfs(0,0,0)
		
		
		