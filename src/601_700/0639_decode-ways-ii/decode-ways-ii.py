class Solution(object):
    def numDecodings(self, s):
        n = len(s)
        cache = {}
        M = 10 ** 9 + 7
        def dfs(i):
            if i >= n:
                return 1
            if i in cache:
                return cache[i]
            res = 0
            if s[i] == '*':
                res = 9 * dfs(i + 1) % M
                if i + 1 < n and s[i + 1] == '*':
                    res = (res + 15 * dfs(i + 2)) % M
                elif i + 1 < n and s[i + 1] <= '6':
                    res = (res + 2 * dfs(i + 2)) % M
                elif i + 1 < n and s[i + 1] > '6':
                    res = (res + dfs(i + 2)) % M
            else:
                res = dfs(i + 1) % M if s[i] != '0' else 0
                if i + 1 < n and s[i + 1] == '*':
                    if s[i] == '1':
                        res = (res + 9 * dfs(i + 2)) % M
                    elif s[i] == '2':
                        res = (res + 6 * dfs(i + 2)) % M
                elif i + 1 < n and 10 <= int(s[i] + s[i + 1]) <= 26:
                    res = (res + dfs(i + 2)) % M
            cache[i] = res
            return cache[i]
        return dfs(0)


