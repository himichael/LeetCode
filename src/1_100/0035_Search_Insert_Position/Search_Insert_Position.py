class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)
			
	#新的实现方式		
    def searchInsert_2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums)-1
        while(start <= end):
            mid = (start+end)/2
            if(nums[mid] > target):
                end = mid-1
            elif(nums[mid] < target):
                start = mid+1
            else:
                return mid
        return start
    