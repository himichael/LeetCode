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
                nums_sum = nums[k] + nums[start] + nums[end]
                if( abs(target-nums_sum) < abs(target-res) ):
                    res = nums_sum
                #print min( abs(target-res), abs(target-nums_sum) ),res
                if(nums_sum > target):
                    end -= 1
                elif(nums_sum < target):
                    start += 1
                else:
                    return res
        return res