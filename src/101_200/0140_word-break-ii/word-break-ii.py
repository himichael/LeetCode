class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        if not s:
            return []
        sets = set(wordDict)
        d = dict()
        def dfs(index):
            if index in d:
                return d[index]
            res = []
            n = len(s)
            if index==n:
                res.append("")
            for end in xrange(index+1,n+1):
                word = s[index:end]
                if word in sets:
                    arr = dfs(end)
                    for li in arr:
                        space = "" if li=="" else " "
                        tmp = s[index:end]+space+li
                        res.append(tmp)
            d[index] = res
            return res
        return dfs(0)
		
		
	# 递归，另一种写法
    def wordBreak(self, s, wordDict):
        words = set(wordDict)
        n = len(s)
        res = []
        def dfs(i, ans):
            if i == n:
                res.append(ans[:-1])
                return
            for j in range(i + 1, n + 1):
                tmp = s[i:j]
                if tmp in words:
                    dfs(j, ans + tmp + " ")
        dfs(0, "")
        return res	
		
		
	# 动态规划(超时)
	def wordBreak(self, s, wordDict):
		if not s:
			return []
		sets = set(wordDict)
		n = len(s)
		dp = [[] for _ in xrange(n+1)]
		dp[0] = [""]
		for i in xrange(1,n+1):
			tmp = []
			for j in xrange(i):
				word = s[j:i]
				if dp[j] and word in sets:
					for li in dp[j]:
						tmp.append( (li+" "+word).strip() )
			dp[i] = tmp
		return dp[-1]	