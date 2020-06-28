class Solution(object):
	def findRepeatedDnaSequences(self, s):
		"""
		:type s: str
		:rtype: List[str]
		"""
		if not s:
			return []
		n = len(s)
		L = 10
		seen = set()
		res = set()
		for i in xrange(n-L+1):
			tmp = s[i:i+L]
			if tmp in seen:
				res.add(tmp)
			seen.add(tmp)
		return list(res)
		
		
		
	# 利用 Rabin-Karp算法思想
	def findRepeatedDnaSequences(self, s):
		"""
		:type s: str
		:rtype: List[str]
		"""
		if not s:
			return []
		n = len(s)
		L = 10
		aL = 4**10
		hash = 0
		seen = set()
		res = set()
		to_int = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
		nums = [to_int[s[i]] for i in xrange(n)]
		for i in xrange(n-L+1):
			if i!=0:
				hash = hash*4 - nums[i-1]*aL + nums[i+L-1]
			else:
				for j in xrange(L):
					hash = hash * 4 + nums[j]
			if hash in seen:
				res.add(s[i:i+L])
			seen.add(hash)
		return list(res)	
		
		