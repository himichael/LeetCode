class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        if not intervals:
            return 0
        intervals = sorted(intervals, key=lambda x:x[1])
        n = len(intervals)
        ans = 1
        right = intervals[0][1]
        for i in xrange(1,n):
            if right <= intervals[i][0]:
                right = intervals[i][1]
                ans += 1
        return n - ans