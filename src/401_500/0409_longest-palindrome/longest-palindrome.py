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
			if i not in d:
				d[i] = 1
			else:
				d[i] += 1
		res = 0
		is_include_even = False
		for i in d:
			if d[i]%2==0:
				res += d[i]
			else:
				tmp = d[i] - (d[i]%2)
				res += tmp
				is_include_even = True
		if is_include_even:
			res += 1
		return res