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