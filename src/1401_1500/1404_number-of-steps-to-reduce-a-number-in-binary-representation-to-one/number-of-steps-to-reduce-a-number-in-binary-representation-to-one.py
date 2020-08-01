class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = int(s,2)
        res = 0
        while n!=1:
            if n&1==1:
                n += 1
                res += 1
            else:
                n //= 2
                res += 1
        return res
