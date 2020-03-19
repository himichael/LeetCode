class Solution(object):
	def longestPalindrome(self, s):
		"""
		:type s: str
		:rtype: int
		"""	
		if not s:
			return 0		
		d = dict()
		for i in s:
			d[i] = d.setdefault(i,0) +1
		res = 0
		is_include_even = False
		for i in d:
			if d[i]%2==0:
				res += d[i]
			else:
				res += d[i]-1
				is_include_even = True
		return res+1 if is_include_even else res
		
		
		
	# 精简实现	
	def longestPalindrome(self, s):
		if not s:
			return 0		
		d = dict()
		res = 0
		for i in s:
			d[i] = d.setdefault(i,0)+1
		for i in d:
			res += d[i]-(d[i]&1)
		return res+1 if res<len(s) else res