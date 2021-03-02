class Solution(object):
    def partition(self, s):
        if not s:
            return []
        res = []
        d = {}
        def is_palindrome(s):
            if s in d:
                return d[s]
            i,j = 0,len(s) - 1
            while i < j:
                if s[i] != s[j]:
                    d[s] = False
                    return False
                i += 1
                j -= 1
            d[s] = True
            return True
        def dfs(s, arr):
            if not s:
                res.append(arr[:])
                return 
            for i in range(len(s)):
                tmp = s[:i + 1]
                if not is_palindrome(tmp):
                    continue
                dfs(s[i + 1:], arr + [tmp])
        dfs(s, [])
        return res