public class Solution {
    public int lengthOfLIS(int[] nums) {
		if(nums==null) {
			return 0;
		}
		int[][] memo = new int[nums.length+1][nums.length];
		for(int[] arr: memo) {
			java.util.Arrays.fill(arr,-1);
		}
		return recursion(nums,-1,0,memo);
    }
	
	int recursion(int[] nums, int pre, int cur, int[][] memo) {
		if(cur==nums.length) {
			return 0;
		}
		if(memo[pre+1][cur] >= 0) {
			return memo[pre+1][cur];
		}
		int take = 0;
		if(pre<0 || nums[cur]>nums[pre]) {
			take = recursion(nums,cur,cur+1,memo)+1;
		}
		int not_take = recursion(nums,pre,cur+1,memo);
		memo[pre+1][cur] = Math.max(take,not_take);
		return memo[pre+1][cur];
	}
}