class Solution(object):
	def containsNearbyDuplicate(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: bool
		"""
		if(not nums or len(nums)==0):
			return False
		d = dict()
		for i in range(len(nums)):
			if(d.has_key(nums[i])):
				d[nums[i]].append(i)
			else:
				d[nums[i]] = [i]
		
		values = d.values()
		for v in values:
			if(len(v) < 2):
				continue
			i = 0
			j = 1
			n = len(v)
			while(i<n and j<n):
				abs_value = abs(v[i]-v[j])
				if( abs_value > k):
					i += 1
					j += 1
				elif( abs_value <= k):
					return True
		return False