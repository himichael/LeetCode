class Solution(object):
    def merge(self, a, n, b, m):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i=n-1
        j=m-1
        index = n+m-1
        while(i>=0 and j>=0):
            if(a[i] >= b[j]):
                a[index] = a[i]
                i = i-1
            else:
                a[index] = b[j]
                j = j-1
            index = index-1
        while(j>=0):
            a[index] = b[j]
            index = index-1
            j = j-1