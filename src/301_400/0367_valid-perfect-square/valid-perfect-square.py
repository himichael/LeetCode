class Solution(object):
	def isPerfectSquare(self, num):
		"""
		:type num: int
		:rtype: bool
		"""
		if num<0:
			return False
		if num==0 or num==1:
			return True
		begin,end = 1,num
		while begin<=end:
			mid = (begin+end)/2
			if mid*mid>num:
				end = mid-1
			elif mid*mid<num:
				begin = mid+1
			else:
				return True
		return False