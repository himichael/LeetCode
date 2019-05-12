class Solution(object):
    def intersect(self, nums1, nums2):
        inter = set(nums1) & set(nums2)
        res = []
        for i in inter:
            res += [i] * min(nums1.count(i), nums2.count(i))  
        return res