class Solution(object):
    def sortArrayByParityII(self, A):
        if not A:
            return []
        n = len(A)
        res = [0] * n
        i = 0
        for x in A:
            if x%2==0:
                res[i] = x
                i += 2
        i = 1
        for x in A:
            if x%2==1:
                res[i] = x
                i += 2
        return res