class Solution {
    public int maxProduct(int[] nums) {
		//定义dp数组，dp[i][0]表示当前最大值，dp[i][1]表示当前最小值
		int[][] dp = new int[nums.length][2];
		dp[0][0] = nums[0];
		dp[0][1] = nums[0];
		int res = nums[0];
		for(int i=1;i<nums.length;i++) {
			//如果nums[i]大于0，dp[i][0]就等于上一个的最大值*nums[i]
			//同样如果nums[i]小于0，dp[i][1]就等于上一个的最小值*nums[i]
			if(nums[i] > 0) {
				dp[i][0] = Math.max(dp[i-1][0]*nums[i], nums[i]);
				dp[i][1] = Math.min(dp[i-1][1]*nums[i], nums[i]);
			}
			else {
				dp[i][0] = Math.max(dp[i-1][1]*nums[i], nums[i]);
				dp[i][1] = Math.min(dp[i-1][0]*nums[i], nums[i]);
			}
			//每次统计出最大值
			res = Math.max(res,dp[i][0]);
		}
        return res;
    }
}