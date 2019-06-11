class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if(nums==None or len(nums)<4):
            return []
        nums.sort()
        res = []
        for i in range(len(nums)-3):
            if(i>0 and nums[i]==nums[i-1]):
                continue
            for j in range(i+1,len(nums)-2):
                if(j-i>1 and nums[j]==nums[j-1]):
                    continue
                start = j+1
                end = len(nums)-1
                while(start < end):
                    x = nums[i]+nums[j]+nums[start]+nums[end]
                    if(x > target):
                        end -= 1
                    elif(x < target):
                        start += 1
                    else:
                        while(start<end and nums[end]==nums[end-1]):
                            end -=1
                        while(start<end and nums[start]==nums[start+1]):
                            start += 1
                        res.append( [nums[i],nums[j],nums[start],nums[end]] )
                        end -=1
                        start += 1
        return res