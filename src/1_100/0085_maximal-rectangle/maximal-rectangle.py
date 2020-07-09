class Solution(object):
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0
        n = len(matrix)
        m = len(matrix[0])
        dp = [0]*m
        res = 0
        for i in xrange(n):
            for j in xrange(m):
                if matrix[i][j]=="1":
                    dp[j] = dp[j]+1
                else:
                    dp[j] = 0
            res = max(res, self.helper(dp) )
        return res

    def helper(self,arr):
        if not arr:
            return 0
        stack = []
        arr = [0] + arr + [0]
        n = len(arr)
        res = 0
        for i in xrange(n):
            while stack and arr[stack[-1]]>arr[i]:
                res = max(res, arr[stack.pop()]*(i-stack[-1]-1))
            stack.append(i)
        return res