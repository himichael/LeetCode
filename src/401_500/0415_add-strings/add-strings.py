class Solution(object):
	def addStrings(self, num1, num2):
		"""
		:type num1: str
		:type num2: str
		:rtype: str
		"""
		if(num1==None or len(num1)==0):
			return num2
		if(num2==None or len(num2)==0):
			return num1
		num_map = {"0":0, "1":1, "2":2, "3":3 ,"4":4, "5":5, "6":6, "7":7, "8":8, "9":9}
		i = len(num1)-1
		j = len(num2)-1
		res = ""
		is_plus = False
		while(i>=0 or j>=0):
			tmp = 0
			if(i >= 0):
				tmp += num_map[ num1[i] ]
			if(j >= 0):
				tmp += num_map[ num2[j] ]
			if(is_plus):
				tmp += 1
				if(tmp > 9):
					is_plus = True
					tmp %= 10
				else:
					is_plus = False
			else:
				if(tmp > 9):
					is_plus = True
					tmp %= 10
			res = str(tmp) + res
			i -= 1
			j -= 1
		if(is_plus):
			return "1"+res
		return res