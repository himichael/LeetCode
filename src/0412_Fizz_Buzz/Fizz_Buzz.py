﻿class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        a=[]
        for i in range(1,n+1):
            if i%3==0:
                if i%5==0:
                    a.append("FizzBuzz")
                else:
                    a.append("Fizz")
            elif i%5==0:
                if i%3==0:
                    a.append("FizzBuzz")
                else:
                    a.append("Buzz")
            else:
                a.append(str(i))
        return a