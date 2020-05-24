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
        
   
   # O(log min(N,M)) 实现方式
	def findMedianSortedArrays(self, nums1, nums2):
		"""
		:type nums1: List[int]
		:type nums2: List[int]
		:rtype: float
		"""		
		if len(nums1)>len(nums2):
			return self.findMedianSortedArrays(nums2,nums1)
		m,n = len(nums1),len(nums2)
		begin,end = 0,m
		left_max,right_min = float("-inf"),float("inf")
		while begin<=end:
			i = begin+(end-begin)/2
			j = (m+n+1)/2 - i
			if i>0 and j<n and nums1[i-1]>nums2[j]:
				end = i-1
			elif j>0 and i<m and nums2[j-1]>nums1[i]:
				begin = i+1
			else:
				if i==0:
					left_max = nums2[j-1]
				elif j==0:
					left_max = nums1[i-1]
				else:
					left_max = max(nums1[i-1],nums2[j-1])
				
				if (n+m)%2:
					return float(left_max)
				
				if i==m:
					right_min = nums2[j]
				elif j==n:
					right_min = nums1[i]
				else:
					right_min = min(nums1[i],nums2[j])
				return (left_max+right_min)/2.0
		return 0.0
		
		
		
	# 另一种实现方式，找最小的k，时间 复杂度为 O(log(m+n))
    def findMedianSortedArrays(self, nums1, nums2):
        def getKthElement(k):        
            index1, index2 = 0, 0
            while True:
                # 特殊情况
                if index1 == m:
                    return nums2[index2 + k - 1]
                if index2 == n:
                    return nums1[index1 + k - 1]
                if k == 1:
                    return min(nums1[index1], nums2[index2])

                # 正常情况
                newIndex1 = min(index1 + k // 2 - 1, m - 1)
                newIndex2 = min(index2 + k // 2 - 1, n - 1)
                pivot1, pivot2 = nums1[newIndex1], nums2[newIndex2]
                if pivot1 <= pivot2:
                    k -= newIndex1 - index1 + 1
                    index1 = newIndex1 + 1
                else:
                    k -= newIndex2 - index2 + 1
                    index2 = newIndex2 + 1
        
        m, n = len(nums1), len(nums2)
        totalLength = m + n
        if totalLength % 2 == 1:
            return getKthElement((totalLength + 1) // 2)/1.0
        else:
            return (getKthElement(totalLength // 2) + getKthElement(totalLength // 2 + 1)) / 2.0
		
		
		