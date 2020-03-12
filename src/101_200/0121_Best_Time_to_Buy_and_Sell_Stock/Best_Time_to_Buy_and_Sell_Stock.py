class Solution(object):
	# 贪心
	def maxProfit(self, prices):
		"""
		:type prices: List[int]
		:rtype: int
		"""
		if(prices==None or len(prices)==0):
			return 0
		min_v = prices[0]
		max_v = 0
		for i in range(len(prices)):
			min_v = min(min_v,prices[i])
			max_v = max(max_v,prices[i]-min_v)
		return max_v
		
		
		
	# 动态规划二维数组
	def maxProfit(self, prices):
		"""
		:type prices: List[int]
		:rtype: int
		"""
		if not prices:
			return 0
		n = len(prices)
		dp = [[0]*2 for _ in xrange(n)]
		dp[0][0] = 0
		dp[0][1] = -prices[0]
		res = 0
		for i in xrange(1,n):
			dp[i][0] = max(dp[i-1][0],dp[i-1][1]+prices[i])
			dp[i][1] = max(dp[i-1][1],-prices[i])
			res = max(res,dp[i][0],dp[i][1])
		return res
		
		
		
	# 动态规划，两个一维数组	
	def maxProfit(self, prices):
		"""
		:type prices: List[int]
		:rtype: int
		"""
		if not prices:
			return 0
		n = len(prices)
		sell = [0 for _ in xrange(n)]
		buy  = [0 for _ in xrange(n)]
		sell[0] = 0
		buy[0] = -prices[0]
		res = 0
		for i in xrange(1,n):
			sell[i] = max(sell[i-1],buy[i-1]+prices[i])
			buy[i]  = max(buy[i-1],-prices[i])
			res = max(res,sell[i],buy[i])
		return res		
		
		
		
	# 动态规划O(1)	
	def maxProfit(self, prices):
		"""
		:type prices: List[int]
		:rtype: int
		"""
		if not prices:
			return 0
		dp0 = 0
		dp1 = -prices[0]
		n = len(prices)
		res = 0
		for i in xrange(1,n):
			dp0 = max(dp0,dp1+prices[i])
			dp1 = max(dp1,-prices[i])
			res = max(res,dp0,dp1)
		return res		
		
		
	# 递归(超时)
	def maxProfit(self, prices):
		if not prices:
			return 0
		self.res = 0
		n = len(prices)
		def dfs(index):
			if n==index:
				return
			for i in xrange(index+1,n):
				if (prices[i]-prices[index])>self.res:
					self.res = prices[i]-prices[index]
			dfs(index+1)
		dfs(0)
		return self.res
		
		
		
	# 递归+记忆化(超时)
	def maxProfit(self, prices):
		if not prices:
			return 0
		self.res = 0
		n = len(prices)
		mem = [-1 for _ in xrange(n)]
		def dfs(index):
			if index==n:
				return
			if mem[index]>-1:
				return mem[index]
			for i in xrange(index+1,n):
				if prices[i]-prices[index]>self.res:
					self.res = prices[i]-prices[index]
			mem[index] = self.res
			dfs(index+1)
		dfs(0)
		return self.res
	
		
		
		
		
		
		
		
		
		