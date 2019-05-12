class Solution(object):
    def removeDuplicates(self, a):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        for j in range(len(a)):
            if(a[i] != a[j]):
                i = i+1
                a[i] = a[j]
        return i+1