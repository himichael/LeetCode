class Solution(object):
    def magicTower(self, nums):
        if sum(nums) < 0:
            return -1
        import heapq
        n = len(nums)
        arr = []
        total = 1
        ans = 0
        for i in range(n):
            if nums[i] < 0:
                heapq.heappush(arr, nums[i])
            total += nums[i]
            while total <= 0:
                total += -heapq.heappop(arr)
                ans += 1
        return ans