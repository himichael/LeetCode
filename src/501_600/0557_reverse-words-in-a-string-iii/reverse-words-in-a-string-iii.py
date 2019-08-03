class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if(s==None or len(s)==0):
            return s
        arr = s.split(" ")
        res = ""
        for n in range(len(arr)):
            k = list(arr[n])
            i = 0
            j = len(k)-1
            while(i <= j):
                k[i],k[j] = k[j],k[i]
                i += 1
                j -= 1
            res = res + "".join(k)
            if(n < len(arr)-1):
                res += " "
        return res