public class Solution {
    public boolean canJump(int[] nums) {
		if(nums==null) {
			return true;
		}
		int n = nums.length;
		int[] memo = new int[n];
		memo[n-1]=1;
		for(int i=n-2;i>=0;--i) {
			int can_jump = Math.min(nums[i]+i,n-1);
			for(int j=i+1;j<=can_jump;++j) {
				if(memo[j]==1) {
					memo[i] = 1;
					break;
				}
			}
		}
		return memo[0]==1;
    }
}
