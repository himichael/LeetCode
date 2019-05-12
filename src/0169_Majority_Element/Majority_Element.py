﻿class Solution(object):
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
        