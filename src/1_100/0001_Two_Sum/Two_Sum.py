﻿class Solution(object):
    def twoSum(self, arr, target):
		#用一个字典记录每个元素的值，以及下标	
		d = {}
		for i,v in enumerate(arr):
			d[v] = i
		
		for i,v in enumerate(arr):
			x = target - v
			#如果target-v的值在字典中，并且这个值的下标和i不同，就是要求的值
			if(d.has_key(x) and i!=d[x]):
				return [d[x],i]
		return []	
		
		
		
	# 一遍hash的实现方式，边加入值 边遍历，一次循环就可以搞定
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums or len(nums)==0:
            return [-1,-1]
        d = dict()
        for i,v in enumerate(nums):
            n = target-v
            if d.has_key(n):
                return [i,d[n]]
            d[v] = i
        return [-1,-1]