class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        if not coins:
            return 1 if amount==0 else 0
        dp = [0 for i in xrange(amount+1)]
        dp[0] = 1
        for c in coins:
            for i in xrange(c,amount+1):
                dp[i] += dp[i-c]
        return dp[-1]
		
		
		
	# 回溯的解法，超时！！！	
	def change(self, amount, coins):
		"""
		:type amount: int
		:type coins: List[int]
		:rtype: int
		"""			
		if not coins:
			return 1 if amount==1 else 0
		self.res = 0
		n = len(coins)
		def f(index,remain):
			if remain==0:
				self.res += 1
				return
			if index<n and remain<coins[index]:
				return
			for i in xrange(index,n):
				f(i,remain-coins[i])
		f(0,amount)
		return self.res
		
		
	# 递归+记忆化的解法， 超时！！！	
	def change(self, amount, coins):
		"""
		:type amount: int
		:type coins: List[int]
		:rtype: int
		"""
		if not coins:
			return 1 if amount==0 else 0
		mem = [ [0]*(amount+1) for i in xrange(len(coins)+1) ]
		def f(index,n):
			if n==0:
				return 1
			if n<0 or index==len(coins):
				return 0
			if mem[index][n]>0:
				return mem[index][n]
			a = f(index,n-coins[index])
			b = f(index+1,n)
			mem[index][n] = a+b
			return a+b
		return f(0,amount)
		
		
		
		
		
		
		
		
		
		