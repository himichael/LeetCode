class Solution {
	public boolean canPartition(int[] nums) {
		if(nums==null){
			return false;
		}
		int total = 0;
		for(int i : nums) {
			total += i;
		}
		if(total%2==1) {
			return false;
		}
		total /= 2;
		int[][] mem = new int[nums.length][total+1];
		for(int i=0;i<nums.length;i++) {
			java.util.Arrays.fill(mem[i],-1);
		}
		return dfs(mem,nums,0,total);
	}
	
	boolean dfs(int[][] mem, int[] nums, int index, int sum) {
		if(sum==0) {
			return true;
		}
		if(sum<0 || index==nums.length) {
			return false;
		}
		if(mem[index][sum]!=-1) {
			return mem[index][sum]==1;
		}
		boolean a = dfs(mem, nums, index+1, sum-nums[index]);
		boolean b = dfs(mem, nums, index+1, sum);
		mem[index][sum] = (a||b)? 1 : 0;
		return mem[index][sum]==1;
	}
}		