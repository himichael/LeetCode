class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        arr = map(lambda x:x*x,A)
        arr.sort()
        return arr