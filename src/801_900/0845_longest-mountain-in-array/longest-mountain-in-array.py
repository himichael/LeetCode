class Solution(object):
    def longestMountain(self, A):
        if not A:
            return 0
        n = len(A)
        left = [0]*n
        right = [0]*n
        res = 0
        for i in xrange(1,n):
            left[i] = left[i-1]+1 if A[i]>A[i-1] else 0
        for i in xrange(n-2,-1,-1):
            right[i] = right[i+1]+1 if A[i]>A[i+1] else 0
        for i in xrange(n):
            if left[i]>0 and right[i]>0:
                res = max(res,left[i]+right[i]+1)
        return res