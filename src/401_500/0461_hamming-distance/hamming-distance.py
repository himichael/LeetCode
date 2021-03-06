﻿class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        a = bin(x)[2:]
        b = bin(y)[2:]
        if(len(a) != len(b)):
            fill_zero = abs(len(a) - len(b))*"0"
            if(len(a) < len(b)):
                a = fill_zero + a
            if(len(a) > len(b)):
                b = fill_zero + b
        i = len(a)-1
        j = len(b)-1
        result = 0
        while(i>=0 and j>=0):
            if(a[i] != b[j]):
                result += 1
            i -= 1
            j -= 1
        return result
    
    #新的实现方式
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x^y).count("1")	



    def hammingDistance(self, x, y):
        xor = x ^ y
        res = 0
        while xor:
            if xor&1==1:
                res += 1
            xor >>= 1
        return res		