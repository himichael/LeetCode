class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d=list(s)
        if(len(d)==0):
            return -1
        x={}
        for i in range(len(d)):
            if d[i] not in x:
                x[d[i]]=1
            else:
                x[d[i]]+=1
        index=-1
        for i in range(len(d)):
            if x[d[i]]==1:
                index=i
                break
        return index

    #另一种实现方式
    def firstUniqChar_2(self, s):
        """
        :type s: str
        :rtype: int
        """
        if(s==None or len(s)==0):
            return -1
        d = dict()
        for i in s:
            if(d.has_key(i)):
                d[i] += 1
            else:
                d[i] = 1
        for j in range(len(s)):
            if(d[s[j]] == 1):
                return j
        return -1