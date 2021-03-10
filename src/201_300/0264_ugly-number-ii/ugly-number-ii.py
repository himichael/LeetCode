class Solution(object):
    def nthUglyNumber(self, n):
        nums = [1]
        i2, i3, i5 = 0,0,0
        for i in range(1,1690):
            tmp = min(nums[i2] * 2, nums[i3] * 3, nums[i5] * 5)
            nums.append(tmp)
            if tmp == nums[i2] * 2:
                i2 += 1
            if tmp == nums[i3] * 3:
                i3 += 1
            if tmp == nums[i5] * 5:
                i5 += 1
        return nums[n - 1]