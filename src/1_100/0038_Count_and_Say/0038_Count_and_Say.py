﻿class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str    
        """
        if(n==1): return "1"
        if(n==2): return "11"
        def recursion(num,res):
            if(num == n-1):
                return res
            i,j = 0,1
            size = len(res)
            tmp = ""
            while(i < size):
                while(j<size and res[i]==res[j]):
                    j += 1
                x = j - i
                tmp = tmp + str(x) + str(res[i])
                i = j
            return recursion(num+1,tmp)
        return recursion(0,"1") 