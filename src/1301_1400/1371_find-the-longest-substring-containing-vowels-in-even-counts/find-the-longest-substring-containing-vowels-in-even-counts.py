class Solution(object):
	def findTheLongestSubstring(self, s):
		if not s:
			return 0
		dp = [-1]*32
		dp[0] = 0
		ans = 0
		status = 0
		for i in xrange(len(s)):
			if s[i]=="a":
				status ^= 1
			elif s[i]=="e":
				status  ^= 2
			elif s[i]=="i":
				status ^= 4
			elif s[i]=="o":
				status ^= 8
			elif s[i]=="u":
				status ^= 16
			
			if dp[status]>=0:
				ans = max(ans,i+1-dp[status])
			else:
				dp[status] = i+1
		return ans
