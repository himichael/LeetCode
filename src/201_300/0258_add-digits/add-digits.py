class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        def recursion(n):
            if(n < 10):
                return n
            tmp = 0
            while(n > 0):
                tmp += n%10
                n /= 10
            return recursion(tmp)
        return recursion(num)
		
		
		
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while(num >= 10):
            tmp = 0
            while(num > 0):
                tmp += num%10
                num /= 10
            num = tmp
        return num  