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