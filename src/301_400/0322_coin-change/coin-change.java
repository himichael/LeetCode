class Solution {
    public int coinChange(int[] coins, int amount) {
		if(coins==null || coins.length==0) {
			return -1;
		}
		if(amount==0) {
			return 0;
		}
		
		int[] dp = new int[amount+1];
		for(int i=0;i<dp.length;i++) {
			dp[i] = amount+1;
		}
		dp[0] = 0;
		for(int i=0;i<=amount;i++) {
			for(int j=0;j<coins.length;j++) {
				if(coins[j] <= i) {
					dp[i] = Math.min(dp[i], dp[i-coins[j]]+1);
					//if(dp[i-coins[j]] < amount) {
					//	dp[i] = dp[i-coins[j]]+1;
					//}
				}
				
			}
		}
		int res = dp[amount];
		return res>amount? -1 : res;
    }
}