class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        res = 0
        if( (dividend>0 and divisor<0) or (dividend<0 and divisor>0) ):
            res = -(abs(dividend)/abs(divisor))
        else:
            res= abs(dividend)/abs(divisor)
        if(res < -2147483648):
            return -2147483648
        elif(res > 2147483647):
            return 2147483647
        else:
            return res