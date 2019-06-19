class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [0 for i in range(target+1)]
        dp[0] = 1
        for i in range(1,target+1):
            for j in nums:
                if(i >= j):
                    dp[i] += dp[i-j]
        return dp[target]
		
	# dfs会超时，当target很大的时候空间复杂度会非常高
	def combinationSum4_2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = []
        #result = [0]
        def back_trace(tmp_num,tmp_arr):
            if(tmp_num==target):
                res.append(list(tmp_arr))
                #result[0] += 1
                return
            for i in range(len(nums)):
                if(tmp_num+nums[i] <= target):
                    tmp_arr.append(nums[i])
                    back_trace(tmp_num+nums[i], tmp_arr)
                    tmp_arr.pop()
        back_trace(0, [])            
        #return result[0]
        return res