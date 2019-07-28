class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if(s==None or len(s)==0 or t==None or len(t)==0):
            return True if(s==t) else False   
        d = dict()
        for i in s:
            if(d.has_key(i)):
                d[i] += 1
            else:
                d[i] = 1
        for j in t:
            if(d.has_key(j)):
                d[j] -= 1
                if(d[j] == 0):
                    del d[j]
            else:
                return False
        return len(d)==0