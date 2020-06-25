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
		
		
	# 递归+记忆化
	def wordBreak(self, s, wordDict):
		if not s:
			return True
		n = len(s)
		d = dict()
		sets = set(wordDict)
		def dfs(s):
			if s in d:
				return d[s]
			if not s:
				return True
			for i in xrange(1,len(s)+1):
				word = s[:i]
				if word in sets:
					if dfs(s[i:]):
						return True
			d[s] = False
			return False
		return dfs(s)

		