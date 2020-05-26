class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set()
        for i in nums:
            if(i in s):
                return i
            s.add(i)
        return -1
		
	# 二分实现，n+1个整数，范围是[1,n]，[1,target-1]都满足cnt[i]<=i
	# [target,n]里的数都满足cnt[i]>i，具有单调性
    def findDuplicate(self, nums):
        n = len(nums)
        begin = 0
        end = n-1
        ans = -1
        while begin<=end:
            mid = begin+(end-begin)//2
            cnt = 0
            for i in xrange(n):
                if nums[i]<=mid:
                    cnt += 1
            if cnt<=mid:
                begin = mid+1
            else:
                end = mid-1
                ans = mid
        return ans
	
	
	
	# Floyd 判圈算法，类似 环形链表 II 这道题
    def findDuplicate(self, nums):
        slow = nums[0]
        fast = nums[nums[0]]
        while slow!=fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        slow = 0
        while slow!=fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	