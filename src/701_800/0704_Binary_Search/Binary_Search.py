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