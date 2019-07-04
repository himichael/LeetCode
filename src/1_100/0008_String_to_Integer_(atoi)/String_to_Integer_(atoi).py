class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if(str==None or len(str)==0 or str==""):
            return 0
        d = {'0':0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9}
        i = 0
        size = len(str)
        isNegative = False
        res = 0
        max_value = 2**31-1
        min_value = -(2**31)
        while(i<size and str[i]==' '):
            i += 1
        if(i<size and str[i]=='-'):
            isNegative = True
            i += 1
        elif(i<size and str[i]=='+'):
            i += 1
        elif(i<size and (str[i]<'0' or str[i]>'9')):
            return 0
        while(i<size and str[i]>='0' and str[i]<='9'):
            res = res*10 + d[str[i]]
            if(res > max_value and not isNegative):
                return max_value
            if(-res < min_value):
                return min_value
            i += 1
        if(isNegative):
            return -res
        return res
    