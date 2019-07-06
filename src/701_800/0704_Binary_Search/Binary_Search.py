class Solution(object):
	def search(self, nums, target):
		begin = 0
		end = len(nums)-1
		while(begin<=end):
			middle = (begin+end)/2
			if(nums[middle] > target):
				end = middle-1
			elif(nums[middle] < target):
				begin = middle+1
			else:
				return middle
		return -1
		
	def search_2(self, nums, target):
		if(nums==None or len(nums)==0):
		return -1
		def recursive(begin,end):
			if(begin > end):
				return -1
			mid = (begin+end)/2
			if(target > nums[mid]):
				return recursive(mid+1,end)
			elif(target < nums[mid]):
				return recursive(begin,mid-1)
			else:
				return mid
			return recursive(0,len(nums)-1)