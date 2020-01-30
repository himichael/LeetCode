class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        if not coins:
            return 1 if amount==0 else 0
        dp = [0 for i in xrange(amount+1)]
        dp[0] = 1
        for c in coins:
            for i in xrange(c,amount+1):
                dp[i] += dp[i-c]
        return dp[-1]