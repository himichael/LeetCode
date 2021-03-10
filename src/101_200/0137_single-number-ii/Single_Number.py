class Solution:
    def singleNumber(self, nums):
        #a = 0
        #b = 0
        #for i in nums:
        #    a = ~b & (a ^ i)
        #    b = ~a & (b ^ i)
        #return a
        return (3 * sum(set(nums)) - sum(nums)) // 2