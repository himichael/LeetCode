class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if(s==None or len(s)==0):
            return 0
        stack = [-1]
        res = 0
        for i in range(len(s)):
            if(s[i] == '('):
                stack.append(i)
            else:
                stack.pop()
                if(not stack):
                    stack.append(i)
                else:
                    res = max(i-stack[len(stack)-1], res)
        return res
		
		
	# DP 解法	
	def longestValidParentheses(self, s):
		if not s:
			return 0
		n = len(s)
		dp = [0 for _ in xrange(n)]
		res = 0
		for i in xrange(n):
			if s[i]==")":
				if i>0 and s[i-1]=="(":
					dp[i] = dp[i-2]+2
				elif i>0 and s[i-1]==")" and i-dp[i-1]-1>=0 and s[i-dp[i-1]-1]=="(":
					dp[i] = dp[i-1] + dp[i-dp[i-1]-2] + 2
				if dp[i]>res:
					res = dp[i]
		return res