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