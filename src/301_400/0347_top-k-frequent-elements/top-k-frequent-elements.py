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
		


	# 桶排序
	def topKFrequent(self, nums, k):
		if not nums or k<=0:
			return []
		if len(nums)<=k:
			return nums
		d = dict()
		for i in nums:
			d[i] = d.setdefault(i,0)+1
		arr = [[] for _ in xrange(len(nums)+1)]
		for key in d.keys():
			i = d[key]
			arr[i].append(key)
		res = []
		j = len(arr)-1
		while j>=0 and len(res)<k:
			if len(arr[j])>0:
				res.extend(arr[j])
			j -= 1
		return res
		
		