class Solution(object):
	def countSubstrings(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		if not s:
			return 0
		n = len(s)
		res = 0
		def check(i,j):
			cnt = 0
			while i>=0 and j<n and s[i]==s[j]:
				i -= 1
				j += 1
				cnt += 1
			return cnt
		for i in xrange(n):
			res += check(i,i)
			res += check(i,i+1)
		return res