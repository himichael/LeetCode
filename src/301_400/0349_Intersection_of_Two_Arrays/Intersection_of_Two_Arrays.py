class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1).intersection(set(nums2)))

    def intersection_2(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if(nums1==None or nums2==None):
            return []
        s = set()
        res = set()
        for i in nums1:
            s.add(i)
        for j in nums2:
            if(j in s):
                res.add(j)
        return list(res)
		
		
	def intersection_2(self, nums1, nums2):
		"""
		:type nums1: List[int]
		:type nums2: List[int]
		:rtype: List[int]
		"""
		return list( set(nums1)&set(nums2) )		