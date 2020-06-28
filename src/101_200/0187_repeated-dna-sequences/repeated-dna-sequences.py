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