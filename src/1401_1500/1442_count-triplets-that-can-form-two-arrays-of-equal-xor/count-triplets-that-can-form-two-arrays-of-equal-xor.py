class Solution(object):
    def countTriplets(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        if n<2:
            return 0
        res = 0
        for i in xrange(n-1):
            tmp = arr[i]
            for j in xrange(i+1,n):
                tmp ^= arr[j]
                if tmp==0:
                    res += (j-i)
        return res    