class NumArray(object):

    def __init__(self, nums):
        n = len(nums)
        self.dp = [0] * (n + 1)
        for i in range(n):
            self.dp[i + 1] = self.dp[i] + nums[i]


    def sumRange(self, i, j):
        return self.dp[j + 1] - self.dp[i]




# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)