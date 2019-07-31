class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if(a==None or len(a)==0):
            return b
        if(b==None or len(b)==0):
            return a
        if(len(a) != len(b)):
            fill_zero = abs(len(a) - len(b))*"0"
            if(len(a) < len(b)):
                a = fill_zero + a
            else:
                b = fill_zero + b
        is_carry = False
        i = len(a)-1
        j = len(b)-1
        res = ""
        while(i>=0 and j>=0):
            tmp_num = int(a[i]) + int(b[j])
            if(is_carry):
                tmp_num += 1
                if(tmp_num >= 2):
                    tmp_num %= 2
                    is_carry = True
                else:
                    is_carry = False
            else:
                if(tmp_num >= 2):
                    tmp_num %= 2
                    is_carry = True
                else:
                    is_carry = False
            res = str(tmp_num) + res
            i -= 1
            j -= 1
        if(is_carry):
            return "1"+res
        return res
    
    