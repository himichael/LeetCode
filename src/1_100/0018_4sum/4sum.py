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
		
		
		
		
	# 优化代码
	def fourSum(self, nums, target):
		if not nums:
			return []
		nums = sorted(nums)
		n = len(nums)
		res = []
		for k in xrange(n-3):
			if nums[k]+nums[k+1]+nums[k+2]+nums[k+3]>target:
				break
			if k>0 and nums[k-1]==nums[k]:
				continue
			for h in xrange(k+1,n-2):
				if nums[k]+nums[h]+nums[h+1]+nums[h+2]>target:
					break
				if h>k+1 and nums[h-1]==nums[h]:
					continue
				i = h+1
				j = n-1
				while i<j:
					tmp = nums[i]+nums[j]+nums[k]+nums[h]
					if tmp>target:
						j -= 1
						while i<j and nums[j+1]==nums[j]:
							j -= 1
					elif tmp<target:
						i += 1
						while i<j and nums[i-1]==nums[i]:
							i += 1
					else:
						res.append([ nums[i],nums[j],nums[k],nums[h] ])
						i += 1
						j -= 1
						while i<j and nums[i-1]==nums[i]:
							i += 1
						while i<j and nums[j+1]==nums[j]:
							j -= 1
		return res
		
		