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
			
			
			
			
p=Solution()
print"8..e4 => false "+str(p.isNumber("8..e4"))
print" => false "+str(p.isNumber(" "))
print" 0 => true "+str(p.isNumber(" 0 "))
print" 0.1 => true "+str(p.isNumber(" 0.1"))
print" abc => false "+str(p.isNumber(" abc"))
print" 1a => false "+str(p.isNumber(" 1a"))
print" 2e10 => true "+str(p.isNumber(" 2e10"))
print" -90e3 => true "+str(p.isNumber(" -90e3"))
print" 1e => false "+str(p.isNumber(" 1e"))
print" e3 => false "+str(p.isNumber(" e3"))
print" 6e-1 => true "+str(p.isNumber("6e-1"))
print" 99e2.5 => false "+str(p.isNumber("99e2.5"))
print" 53.5e93 => true "+str(p.isNumber("53.5e93"))
print" --6 => false "+str(p.isNumber("--6"))
print" -+3 => false "+str(p.isNumber("-+3"))
print" 95a54e53 => false "+str(p.isNumber("95a54e53"))
print" .1 => true "+str(p.isNumber(".1"))
print" 3. => true "+str(p.isNumber("3."))
print" . => false "+str(p.isNumber("."))
print" -. => false "+str(p.isNumber("-."))
print" -222.33. => false "+str(p.isNumber("-22.33."))
print" -3.1415e99999 => true "+str(p.isNumber("-3.1415e99999"))
print" -3.1415e99a88 => false "+str(p.isNumber("-3.1415e99a88"))