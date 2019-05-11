class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0 or n==1 or n==2:
            return n
        f1 = 1
        f2 = 1
        all_way = 0
        for _ in range(2,n+1):
            all_way = f1+f2
            f1 = f2
            f2 = all_way
        return all_way
            