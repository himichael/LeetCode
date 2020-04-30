class Solution(object):
	def isHappy(self, n):
		"""
		:type n: int
		:rtype: bool
		"""		
		d = dict()
		def cacl_sum(i):
			num = 0
			while i>0:
				num = num + (i%10)*(i%10)
				i //= 10
			return num
		d[n] = 1
		while d[n]<2:
			if n==1:
				return True
			n = cacl_sum(n)
			d[n] = d.setdefault(n,0) + 1
		return False
		
		
		
	# 另一种解法	
	def isHappy(self, n):	
		s = set()
		while n not in s:
			s.add(n)
			n = sum(int(i)**2 for i in str(n))
		return n==1
		
		
		
	# 快慢指针不断收敛	
	def isHappy(self, n):
		def square_sum(i):
			sum = 0
			while i>0:
				sum = sum + (i%10)**2
				i //= 10
			return sum
		low = n
		fast = square_sum(n)
		while low!=fast:
			low = square_sum(low)
			fast = square_sum( square_sum(fast) )
		return low==1	


		