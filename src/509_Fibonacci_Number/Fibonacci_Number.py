class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if(N==0):
            return 0
        if(N==1 or N==2):
            return 1
        
        f1 = 1
        f2 = 1
        for i in range(2,N):
            tmp = f1+f2
            f1 = f2
            f2 = tmp
        return f2