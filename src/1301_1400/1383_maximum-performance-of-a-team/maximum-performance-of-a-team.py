class Solution(object):
    def maxPerformance(self, n, speed, efficiency, k):
        """
        :type n: int
        :type speed: List[int]
        :type efficiency: List[int]
        :type k: int
        :rtype: int
        """
        import heapq
        arr = zip(speed,efficiency)
        arr = sorted(arr,key=lambda x:x[1],reverse=True)
        res = 0
        heap = []
        total_speed = 0
        for s,e in arr:
            heapq.heappush(heap,s)
            if len(heap)>k:
                total_speed -= heapq.heappop(heap)
            total_speed += s
            res = max(res,total_speed*e)
        return res%(10**9+7)
            