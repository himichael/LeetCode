class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return False
        n = len(s)
        i,j = 0,n-1
        while i<n and s[i]==" ":
            i += 1
        while j>=0 and s[j]==" ":
            j -= 1
        if i==j and not (s[i]>='0' and s[i]<='9'):
            return False
        s = s[i:j+1]
        n = len(s)
        i = 0
        if not s:
            return False
        
        if s[i] in ('-','+'):
            i += 1
            if i==n:
                return False
        dot_num = 0
        num_count = 0
        letter = set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.'])
        while i<n and s[i] in letter:
            if s[i]==".":
                dot_num += 1
            else:
                num_count += 1
            i += 1
        if i==n:
            if dot_num==0 or dot_num==1:
                return num_count>0
            else:
                return False
        
        letter.remove(".")
        if s[i]=='e':
            if num_count==0 or dot_num>1:
                return False
            i +=1      
            if i==n:
                return False
            if s[i] in ('-','+'):
                i += 1
                if i==n:
                    return False
            while i<n and s[i] in letter:
                i += 1
            if i==n:
                return True
            return False
        else:
            return False