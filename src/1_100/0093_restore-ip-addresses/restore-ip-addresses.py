class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if(s==None or len(s)<4 or len(s)>12):
            return []
        res = []
        size = len(s)
        def recursion(level,index,arr):
            if(level==4):
                #print str(arr)+ "   index->"+str(index)+"  size->"+str(size)
                if(index == size):
                    tmp = ""
                    for i in arr:
                        tmp = tmp + "." + i
                    res.append( tmp[1:] )
                return
            for j in range(1,4):
                if(index+j > size):
                    break
                x = s[index:index+j]
                if(x.startswith("0") and len(x)>1):
                    continue
                if(int(x)>=0 and int(x)<=255):
                    recursion(level+1, index+j, arr+[x])
        recursion(0,0,[])
        return res
		
	
	
	# 循环实现
	def restoreIpAddresses(self, s):
		if not s:
			return []
		n = len(s)
		i,j,k = 1,1,1
		res = []
		def check(s):
			if not s:
				return False
			num = int(s)
			if len(s)>1 and s.startswith("0"):
				return False
			if 0<=num<=255:
				return True
		while i<n and i<=3:
			j = i
			while j<n and j<=i+3:
				k = j
				while k<n and k<=j+3:
					s1 = s[:i]
					s2 = s[i:j]
					s3 = s[j:k]
					s4 = s[k:]
					if check(s1) and check(s2) and check(s3) and check(s4):
						res.append(s1+"."+s2+"."+s3+"."+s4)
					k += 1
				j += 1
			i += 1
		return res