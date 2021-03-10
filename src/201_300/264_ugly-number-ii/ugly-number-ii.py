class Solution:
    def nthUglyNumber(self, n: int) -> int:
        s = {1}
        q = []
        nums = []
        heapq.heappush(q,1)
        for i in range(1690):
            cur = heapq.heappop(q)
            nums.append(cur)
            for k in (2,3,5):
                tmp = cur * k
                if tmp not in s:
                    s.add(tmp)
                    heapq.heappush(q,tmp)
        return nums[n - 1]
                
