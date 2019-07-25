class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        return x**n

    #分治的实现方式
	def myPow_2(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if(n == 0):
            return 1.0
        if(n == 1):
            return x
        if(n < 0):
            n = -n
            return 1 / self.myPow(x, n)
        else:
            if(n%2 ==0):
                return self.myPow(x*x, n/2)
            else:
                return x * self.myPow(x, n-1)