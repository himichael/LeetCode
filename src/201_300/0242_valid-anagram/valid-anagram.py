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
		
		
		
    def isAnagram__2(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if(s==None or len(s)==0 or t==None or len(t)==0):
            return True if(s==t) else False   
        return sorted(s) == sorted(t)
		
		
			
    def isAnagram_3(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_dict = [0]*26
        t_dict = [0]*26
        for i in s:
            s_dict[ord(i)-ord('a')] += 1
        for j in t:
            t_dict[ord(j)-ord('a')] += 1
        return s_dict == t_dict		