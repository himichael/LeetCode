class Solution:
    def isMatch(self, s, p):
		s_len = len(s)
		p_len = len(p)
		dp = [[False]*(p_len+1) for _ in xrange(s_len+1)]
		dp[0][0] = True
		for i in xrange(1,p_len+1):
			dp[0][i] = dp[0][i-1] and p[i-1]=="*"
		for i in xrange(1,s_len+1):
			for j in xrange(1,p_len+1):
				if s[i-1]==p[j-1] or p[j-1]=="?":
					dp[i][j] = dp[i-1][j-1]
				if p[j-1]=="*":
					dp[i][j] = dp[i-1][j] or dp[i][j-1]
		return dp[-1][-1]
		
		
		
	# 递归+记忆化(超时)
	def isMatch(self, s, p):
		d = dict()
		def check_any(pattern):
			if not pattern:
				return False
			p = pattern.replace("*","")
			return p==""
		def dfs(s,p):
			if (s,p) in d:
				return d[s,p]
			if not p:
				return not s
			if not s:
				d[s,p] = check_any(p)
				return d[s,p]
			match_any = p[0]=="*"
			if match_any:
				d[s,p] = dfs(s[1:],p) or dfs(s,p[1:])
			else:
				first_match = len(s)>0 and p[0] in (s[0],"?")
				d[s,p] = first_match and dfs(s[1:],p[1:])
			return d[s,p]
		return dfs(s,p)
		
		
		