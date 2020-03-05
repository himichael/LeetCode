class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str    
        """
        #解析n-1的情况，然后拼接成一个字符串再递归调用n，最后返回
        def recursion(num,res):
            if(num == n):
                return res
            i,j = 0,1
            size = len(res)
            tmp = ""
            while(i < size):
                while(j<size and res[i]==res[j]):
                    j += 1
                x = j-i
                tmp = tmp + str(x) + res[i]
                i = j
            return recursion(num+1,tmp)
        return recursion(1,"1")
		
		
		
	# 基于循环的实现方式
	def countAndSay(self, n):
		if n<=0:
			return ""
		res = "1"
		for _ in xrange(n-1):	#迭代次数
			flag = res[0]
			count = 0
			s = ""
			for j in xrange(len(res)):
				if flag==res[j]:
					count += 1
				else:
					s = s + str(count) + flag
					flag = res[j]
					count = 1
			# 处理最后一个字符
			s = s + str(count) + flag
			res = s
		return res
		