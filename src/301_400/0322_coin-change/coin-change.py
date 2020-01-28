class Solution(object):
	def coinChange(self, coins, amount):
		"""
		:type coins: List[int]
		:type amount: int
		:rtype: int
		"""	
		if not coins:
			return 0
		mem = [-1] * (amount+1)
		def f(n):
			if n<=0:
				return -1 if n<0 else 0
			res = float("inf")
			if mem[n]>0:
				return mem[n]
			for c in coins:
				if n-c>=0:
					sub = f(n-c)
					if sub>-1:
						res = min(res,sub+1)
			mem[n] = res
			return -1 if res==float("inf") else res
		ans = f(amount)
		return ans if ans>-1 else -1


	# 动态规划
	def coinChange(self, coins, amount):
		"""
		:type coins: List[int]
		:type amount: int
		:rtype: int
		"""	
		if not coins:
			return 0
		dp = [ float("inf") for i in xrange(amount+1) ]
		dp[0] = 0
		for c in coins:
			for i in xrange(c,amount+1):
				dp[i] = min(dp[i],dp[i-c]+1)
		return dp[-1] if dp[-1]!=float("inf") else -1