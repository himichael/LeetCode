class Solution(object):
	def isPalindrome(self, x):
		"""
		:type x: int
		:rtype: bool
		"""
		if(x < 0):
			return False
		if(x == 0):
			return True
		#将数字转换成字符串，i指针从头开始，j指针从尾开始，两两对比，直到j<=i结束
		n = str(x)
		j = len(n)-1
		for i,v in enumerate(n):
			if( (j>i) and (n[i]!=n[j]) ):
				return False
			j = j-1
		return True