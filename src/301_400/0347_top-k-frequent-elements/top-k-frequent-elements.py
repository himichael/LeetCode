class Solution(object):
	def topKFrequent(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: List[int]
		"""		
		if len(nums)<=k:
			return nums
		d = dict()
		for c in nums:
			if c not in d:
				d[c] = [1,c]
			else:
				d[c][0] += 1
		values = d.values()
		values.sort(key=lambda x:x[0],reverse=True)
		res = [values[i][1] for i in xrange(k)]
		return res