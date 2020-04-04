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
		
		
		