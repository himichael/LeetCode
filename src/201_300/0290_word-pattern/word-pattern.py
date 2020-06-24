class Solution(object):
	def wordPattern(self, pattern, str):
		"""
		:type pattern: str
		:type str: str
		:rtype: bool
		"""
		if not (pattern and str):
			return False
		arr = str.split(" ")
		d = dict()
		n = len(pattern)
		if n!=len(arr):
			return False
		for i in xrange(n):
			if pattern[i] not in d:
				if arr[i] in d.values():
					return False
				else:
					d[pattern[i]] = arr[i]
			else:
				if d[pattern[i]]!=arr[i]:
					return False
		return True