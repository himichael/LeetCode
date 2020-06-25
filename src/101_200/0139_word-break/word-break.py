class Solution(object):
	def wordBreak(self, s, wordDict):
		"""
		:type s: str
		:type wordDict: List[str]
		:rtype: bool
		"""
		if not s:
			return True
		n = len(s)
		sets = set(wordDict)
		dp = [False for _ in xrange(n+1)]
		dp[0] = True
		for i in xrange(1,n+1):
			for j in xrange(0,i):
				if dp[j] and s[j:i] in sets:
					dp[i] = True
		return dp[-1]