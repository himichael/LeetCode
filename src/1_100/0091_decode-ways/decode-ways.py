class Solution(object):
    def numDecodings(self, s):
        n = len(s)
        d = {}
        def f(index):
            if index >= n:
                return 1
            if index in d:
                return d[index]
            a,b = 0,0
            if s[index] != '0':
                a = f(index + 1)
            if index + 2 <= n and s[index] != '0' and int(s[index : index + 2]) <= 26:
                b = f(index + 2)
            d[index] = a + b
            return d[index]
        return f(0)
		
		
    def numDecodings(self, s):    
        if not s or s[0] == '0':
            return 0
        if len(s) == 1:
            return 0 if s[0] == '0' else 1
        dp = [0] * len(s)
        dp[0] = 1
        if s[1] == '0':
            if 10 <= int(s[:2]) <= 26:
                dp[1] = 1
            else:
                return 0
        else:
            dp[1] = 2 if 10 <= int(s[:2]) <= 26 else 1
        for i in range(2, len(s)):
            if s[i] == '0':
                if s[i - 1] != '0' and 10 <= int(s[i - 1] + s[i]) <= 26:
                    dp[i] = dp[i - 2]
                else:
                    return 0
            else:
                if s[i - 1] != '0' and 10 <= int(s[i - 1] + s[i]) <= 26:
                    dp[i] = dp[i - 1] + dp[i - 2]
                else:
                    dp[i] = dp[i - 1]
        return dp[-1]