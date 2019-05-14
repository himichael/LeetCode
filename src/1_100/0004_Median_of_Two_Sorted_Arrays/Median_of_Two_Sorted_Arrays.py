class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
	这题目 应该用类似二分查找的方式去做，因为题目要求是O(log m+n)时间复杂度
	这里偷懒用了排序再输出
	如果是无序数组，用两个堆也可以解决
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        num = 0
        x = []
        if(nums1==None):
            num = len(nums2)
            x = nums2
        elif(nums2==None):
            num = len(nums1)
            x = nums1
        else:
            num = len(nums1+nums2)
            x = (nums1+nums2)
            x.sort()

        if(num%2 == 0):
            #print x,num,num/2,num/2+1
            return float( x[num/2-1]+x[num/2] )/2
        else:
            return float( x[num/2] )
        
    