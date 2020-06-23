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
		
		
		
	# 位运算实现
	def addBinary(self, a, b):
		x = int(a,2)
		y = int(b,2)
		while y:
			ans = x^y
			carry = (x&y)<<1
			x,y = ans,carry
		return bin(x)[2:]
		
		
		
	# 精简实现
	def addBinary(self, a, b):
		if not (a and b):
			return a if a else b
		i = len(a)-1
		j = len(b)-1
		carry = 0
		res = ""
		while i>=0 or j>=0:
			t = (int(a[i]) if i>=0 else 0)+(int(b[j]) if j>=0 else 0)+carry
			carry = 1 if t>1 else 0
			t %= 2
			i = i-1 if i>0 else -1
			j = j-1 if j>0 else -1
			res = str(t) + res
		if carry:
			res = "1"+res
		return res
		
		
		
		
		
		
		
		
		
		
    
    