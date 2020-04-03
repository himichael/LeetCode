class Solution(object):
	def findKthLargest(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: int
		"""
		import random
		def partition(left,right,index):
			pivot = nums[index]
			nums[right],nums[index] = nums[index],nums[right]
			j = left
			for i in xrange(left,right):
				if nums[i]<pivot:
					nums[i],nums[j] = nums[j],nums[i]
					j += 1
			nums[right],nums[j] = nums[j],nums[right]
			return j
			
		def select(left,right,k_smallest):
			if left==right:
				return nums[left]
			index = random.randint(left,right)
			poivt_index = partition(left,right,index)
			if k_smallest==poivt_index:
				return nums[k_smallest]
			elif k_smallest>poivt_index:
				return select(poivt_index+1,right,k_smallest)
			else:
				return select(left,poivt_index-1,k_smallest)
		return select(0,len(nums)-1, len(nums)-k)
		
		
		
	# 精简代码
	def findKthLargest(self, nums, k):
		import random
		k_th = len(nums)-k
		def partition(begin,end):
			idx = random.randint(begin,end)
			nums[idx],nums[end] = nums[end],nums[idx]
			povit = nums[end]
			j = begin
			for i in xrange(begin,end):
				if nums[i]<povit:
					nums[i],nums[j] = nums[j],nums[i]
					j += 1
			nums[j],nums[end] = nums[end],nums[j]
			return j
		def select(begin,end):
			if begin==end:
				return nums[begin]
			pos = partition(begin,end)
			if pos==k_th:
				return nums[k_th]
			elif pos>k_th:
				return select(begin,pos-1)
			else:
				return select(pos+1,end)
		return select(0,len(nums)-1)
		
		
		