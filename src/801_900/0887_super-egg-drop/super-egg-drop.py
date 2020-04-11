﻿class Solution(object):
	# 递归(超时)
	def superEggDrop(self, K, N):
		"""
		:type K: int
		:type N: int
		:rtype: int
		"""
		def dfs(k,n):
			if n==0 or n==1 or k==1:
				return n
			min_num = float("inf")
			for i in xrange(1,n+1):
				a = dfs(k-1,i-1)
				b = dfs(k,n-i)
				t_min = max(a,b)+1
				min_num = min(min_num,t_min)
			return min_num
		return dfs(K,N)
		
		
		
	# 递归+备忘录(超时)，时间复杂度O(K*N^2)
	def superEggDrop(self, K, N):
		cache = [[ 0 for _ in xrange(N+1)] for _ in xrange(K+1)]
		def dfs(k,n):
			if n==0 or n==1 or k==1:
				return n
			if cache[k][n]>0:
				return cache[k][n]
			min_num = float("inf")
			for i in xrange(1,n+1):
				a = dfs(k-1,i-1)
				b = dfs(k,n-i)
				t_min = max(a,b)+1
				min_num = min(min_num,t_min)
			cache[k][n] = min_num
			return cache[k][n]
		return dfs(K,N)	
		
		
		
	# 二分法优化+递归+备忘录，时间复杂度O(K*NlogN)
	def superEggDrop(self, K, N):
		cache = dict()
		def dfs(k,n):
			if k==1:
				return n
			if n==0:
				return 0
			if (k,n) in cache:
				return cache[k,n]
			begin = 1
			end = n
			ans = float("inf")
			while begin<=end:
				mid = begin+(end-begin)/2
				broken = dfs(k-1,mid-1)
				not_broken = dfs(k,n-mid)
				if broken>not_broken:
					end = mid-1
					ans = min(ans,broken+1)
				else:
					begin = mid+1
					ans = min(ans,not_broken+1)
			cache[k,n] = ans
			return cache[k,n]
		return dfs(K,N)	
		