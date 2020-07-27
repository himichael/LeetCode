class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type queryTime: int
        :rtype: int
        """
        if not startTime or not endTime:
            return 0
        n = len(startTime)
        res = 0
        for i in xrange(n):
            if startTime[i]<=queryTime<=endTime[i]:
                res += 1
        return res