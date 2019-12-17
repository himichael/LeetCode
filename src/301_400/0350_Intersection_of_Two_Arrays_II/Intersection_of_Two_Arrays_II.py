class Solution(object):
    def intersect(self, nums1, nums2):
        inter = set(nums1) & set(nums2)
        res = []
        for i in inter:
            res += [i] * min(nums1.count(i), nums2.count(i))  
        return res

	def intersect(self, nums1, nums2):
		"""
		:type nums1: List[int]
		:type nums2: List[int]
		:rtype: List[int]
		"""		
		nums1.sort()
		nums2.sort()
		n1,n2 = 0,0
		res = []
		while n1<len(nums1) and n2<len(nums2):
			if nums1[n1]<nums2[n2]:
				n1 += 1
			elif nums1[n1]>nums2[n2]:
				n2 += 1
			else:
				res.append(nums1[n1])
				n1,n2 = n1+1,n2+1
		return res