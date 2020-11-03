class Solution(object):
    def validMountainArray(self, A):
        if not A:
            return False
        N = len(A)
        if N<3:
            return False
        i = 0
        while i<N and A[i]