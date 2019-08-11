class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if(num==1 or num==2 or num==3 or num==5):
            return True
        while(num > 0):
            if(num%2 == 0):
                num /= 2
            elif(num%3 == 0):
                num /=3
            elif(num%5 == 0):
                num /=5
            elif(num == 1):
                return True
            else:
                return False
        return False
		
	
	
	#丑数的递归实现
    def isUgly_2(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if(num==1 or num==2 or num==3 or num==5):
            return True
        def recursion(n):
            if(n == 0):
                return False
            if(n == 1):
                return True
            if(n%2 == 0):
                return recursion(n/2)
            if(n%3 == 0):
                return recursion(n/3)
            if(n%5 == 0):
                return recursion(n/5)
            return False
        return recursion(num)