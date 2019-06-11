class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if(nums==None):
            return 0
        if(len(nums)<=3):
            return sum(nums)
        nums.sort()
        res = nums[0]+nums[1]+nums[2]
        for k in range(len(nums)):
            start = k+1
            end = len(nums)-1
            while(start < end):
                x = nums[k]+nums[start]+nums[end]
                if( abs(target-x) < abs(target-res) ):
                    res = x
                if(x > target):
                    end -= 1
                elif(x < target):
                    start += 1
                else:
                    return res
        return res