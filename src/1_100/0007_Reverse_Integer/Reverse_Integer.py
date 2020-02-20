class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if(x==0):
            return 0
        b=list(str(x))
        c=b[::-1]
        index=0
        minus_sign=len(c)-1
        has_minus=False
        for i in range(len(c)):
            if c[i]!='0':
                break
            index+=1
        if c[len(c)-1]=='-':
            minus_sign-=1
            has_minus=True
        result = int( "".join(c[index:minus_sign+1]) )
        if has_minus:
            result = 0 - result
        if (result<(-2**31) or result>2**31-1):
            result = 0
        return result
		
		
		
	def reverse(self, x):
		arr = list(str(x))
		is_negative = False
		start = 0
		n = len(arr)
		if arr[0] == '-':
			is_negative = True
			start = 1
		i = start
		j = n-1
		while i<j:
			arr[i],arr[j] = arr[j],arr[i]
			i += 1
			j -= 1
		res = int("".join(arr))
		if res<-2**31 or res>(2**31-1):
			return 0
		return res
		
		
		
	def reverse(self, x):
		if x<0:
			x = x*-1
			x = int("-"+str(x)[::-1])
		else:
			x = int(str(x)[::-1])
		if x>(2**31-1) or x<-2**31:
			return 0
		return x