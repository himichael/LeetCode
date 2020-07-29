class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        n = len(cardPoints)
        total = sum(cardPoints)
        min_size = float("inf")
        size = n-k
        tmp = 0
        for i in xrange(n):
            tmp += cardPoints[i]
            if i>=size:
                tmp -= cardPoints[i-size]
            if i>=size-1:
                min_size = min(min_size,tmp)
        return total-min_size