class Solution(object):
	# 排序，再比较前后两数
	def minIncrementForUnique(self, A):
		"""
		:type A: List[int]
		:rtype: int
		"""
		if not A or len(A)<=1:
			return 0
		A = sorted(A)
		count = 0
		pre = A[0]
		for i in xrange(1,len(A)):
			if A[i]<=pre:
				increment = pre-A[i]+1
				count += increment
				pre = A[i] + increment
			else:
				pre = A[i]
		return count
		
	
	
	# 题目说明最大值为4W，可以用计数排序
	def minIncrementForUnique(self, A):
		if not A or len(A)<=1:
			return 0
		n = len(A)
		arr = [0 for _ in xrange(40000+1)]
		max_num = -1
		move = 0
		for i in A:
			arr[i] += 1
			max_num = max(max_num,i)
		for i in xrange(max_num+1):
			if arr[i]>1:
				diff = arr[i]-1
				move += diff
				arr[i+1] += diff
		if arr[max_num]>1:
			diff = arr[max_num+1]-1
			move += (1+diff)*diff/2
		return move
		
		
		