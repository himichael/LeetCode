class Solution(object):
	def findPeakElement(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		begin,end = 0,len(nums)-1
		while begin<end:
			mid = begin+(end-begin)/2
			if nums[mid]>nums[mid+1]:
				end = mid
			else:
				begin = mid+1
		return begin
		
		
	# 另一种写法	
    def findPeakElement(self, nums):
        if not nums or len(nums)==1:
            return -1 if not nums else 0
        n = len(nums)
        begin = 0
        end = n-1
        while begin<=end:
            mid = begin+(end-begin)//2
            if mid==n-1:
                begin = mid
                break
            if nums[mid]>nums[mid+1]:
                end = mid-1
            else:
                begin = mid+1
        return begin