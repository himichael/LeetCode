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