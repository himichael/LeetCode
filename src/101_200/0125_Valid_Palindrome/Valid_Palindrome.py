class Solution(object):
    def isPalindrome(self, a):
        """
        :type s: str
        :rtype: bool
        """
        b=list(a)
        c=[]
        for i in range(len(b)):
            if b[i].isalnum():
                c.append(b[i].lower())
        i=0
        j=len(c)-1
        loop=True
        while j>i:
            if c[i]!=c[j]:
                loop=False
            j-=1
            i+=1
        return loop