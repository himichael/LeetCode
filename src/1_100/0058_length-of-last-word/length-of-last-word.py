class Solution(object):
	def lengthOfLastWord(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		if not s:
			return 0
		arr = s.strip().split(" ")
		return len(arr[-1])