class Solution(object):
	# 暴力(超时)
    def subarraySum(self, nums, k):
        if not nums:
            return 0
        n = len(nums)
        count = 0
        for i in xrange(n):
            sum = 0
            for j in xrange(i,-1,-1):
               sum += nums[j]
               if sum==k:
                   count += 1
        return count

		
		
	# hash+前缀和 	
    def subarraySum(self, nums, k):
        if not nums:
            return 0
        n = len(nums)
        d = dict()
        d[0] = 1
        count = 0
        pre = 0
        for i in xrange(n):
            pre += nums[i]
            if pre-k in d:
                count += d[pre-k]
            d[pre] = d.setdefault(pre,0)+1
        return count
		
		
		
		
		
		
		
		
		
		
		