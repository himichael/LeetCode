class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if(x==0):
            return 0
        b=list(str(x))
        c=b[::-1]
        index=0
        minus_sign=len(c)-1
        has_minus=False
        for i in range(len(c)):
            if c[i]!='0':
                break
            index+=1
        if c[len(c)-1]=='-':
            minus_sign-=1
            has_minus=True
        
        result = int( "".join(c[index:minus_sign+1]) )
        if has_minus:
            result = 0 - result
        if (result<(-2**31) or result>2**31-1):
            result = 0
        return result