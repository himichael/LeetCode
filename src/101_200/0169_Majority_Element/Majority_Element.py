class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = {}
        for i in range(len(nums)):
            if(m.has_key(nums[i])):
                m[nums[i]]+=1
            else:
                m[nums[i]] = 1
        count = len(nums)/2
        for i in m.keys():
            if(m[i] > count):
                return i
        return -1
        
    #一行代码搞定
    def majorityElement_2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sorted(nums)[len(nums)/2]

    #hash实现方式的优化
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums)==1):
            return nums[0]
        m = {}
        half = len(nums)/2
        for i in range(len(nums)):
            if(m.has_key(nums[i])):
                m[nums[i]]+=1
                if(m[nums[i]] > half):
                    return nums[i]
            else:
                m[nums[i]] = 1
        return -1

    #摩尔投票算法    
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        candidate = nums[0]
        count = 1
        for i in range(1,len(nums)):
            if(count == 0):
                candidate = nums[i]
                count = 1
            elif(candidate == nums[i]):
                count += 1
            else:
                count -= 1
        return candidate

        
		
		
		
		
		
		
		
		
		
		
        
