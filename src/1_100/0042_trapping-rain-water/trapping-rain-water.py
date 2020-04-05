class Solution(object):
    def trap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(nums==None or len(nums)==0):
            return 0
        left = 0
        right = len(nums)-1
        res = 0
        while(left < right):
            cur_min = min(nums[left],nums[right])
            if(cur_min == nums[left]):
                left += 1
                while(left<right and nums[left]<=cur_min):
                    res += cur_min - nums[left]
                    left += 1
            else:
                right -= 1
                while(left<right and nums[right]<=cur_min):
                    res += cur_min - nums[right]
                    right -= 1
        return res
		
		
	# 单调栈解法
	def trap(self, height):
		if not height:
			return 0
		stack = []
		ans = 0
		for i in xrange(len(height)):
			while stack and height[stack[-1]]<height[i]:
				pop_idx = stack.pop()
				while stack and height[stack[-1]]==height[pop_idx]:
					stack.pop()
				if stack:
					peek_idx = stack[-1]
					diff = min(height[peek_idx],height[i])-height[pop_idx]
					distance = i-peek_idx-1
					ans += diff*distance
			stack.append(i)
		return ans	
		
		
	# 暴力(超时)
	def trap(self, height):
		if not height:
			return 0		
		N = len(height)
		ans = 0
		for i in xrange(1,N-1):
			left_max,right_max = 0,0
			for j in xrange(i,-1,-1):
				left_max = max(left_max,height[j])
			for k in xrange(i,N):
				right_max = max(right_max,height[k])
			ans += min(left_max,right_max)-height[i]
		return ans	
		
		
	# 动态规划
	def trap(self, height):
		if not height:
			return 0		
		N = len(height)
		ans = 0
		left_max = [0 for _ in xrange(N)]
		right_max = [0 for _ in xrange(N)]
		left_max[0] = height[0]
		right_max[N-1] = height[N-1]
		for i in xrange(1,N):
			left_max[i] = max(left_max[i-1],height[i])
		for i in xrange(N-2,0,-1):
			right_max[i] = max(right_max[i+1],height[i])
		for i in xrange(1,N-1):
			ans += min(left_max[i],right_max[i])-height[i]
		return ans



	# 双指针
	def trap(self, height):
		if not height:
			return 0
		N = len(height)
		ans = 0
		left_max = 0
		right_max = 0
		left = 0
		right = N-1
		while left<right:
			if height[left]<height[right]:
				if height[left]>=left_max:
					left_max = height[left]
				else:
					ans += left_max-height[left]
				left += 1
			else:
				if height[right]>=right_max:
					right_max = height[right]
				else:
					ans += right_max-height[right]
				right -= 1
		return ans
		