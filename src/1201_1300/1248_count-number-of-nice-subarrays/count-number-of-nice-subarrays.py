class Solution(object):
	def numberOfSubarrays(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: int
		"""
		if not nums or k<=0:
			return 0
		n = len(nums)
		dp = [0]*(n+1)
		dp[0] = 1
		ans = 0
		odd = 0
		for num in nums:
			if num%2==1:
				odd += 1
			if odd>=k:
				ans += dp[odd-k]
			dp[odd] += 1
		return ans
		
		
		
	# 滑动窗口解法	
	def numberOfSubarrays(self, nums, k):
		if not nums or k<=0:
			return 0
		n = len(nums)
		left = 0
		right = 0
		odd_cnt = 0
		res = 0
		while right<n:
			if (nums[right]&1)==1:
				odd_cnt += 1
			right += 1
			if odd_cnt==k:
				tmp = right
				while right<n and (nums[right]&1)==0:
					right += 1
				right_event_cnt = right - tmp
				left_event_cnt = 0
				while (nums[left]&1)==0:
					left_event_cnt += 1
					left += 1
				res += (left_event_cnt+1) * (right_event_cnt+1)
				left += 1
				odd_cnt -= 1
		return res
		
		
		