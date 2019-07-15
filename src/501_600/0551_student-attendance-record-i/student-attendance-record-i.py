class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if(s==None or len(s)==0):
            return True
        absent = 0
        if(s.find("LLL")>-1):
            return False
        for i in s:
            if(i=='A'):
                absent += 1
                if(absent >= 2):
                    return False
        return True