class Solution(object):
	def lengthOfLongestSubstring(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		res,i,j = 0,0,0
		letter_set = set()
		size = len(s)
		# 这里使用滑动窗口模式 [i..j] 窗口内的字符，就是最长字串
		while(i<size and j<size):
			if(s[j] not in letter_set):
				letter_set.add(s[j])
				j += 1
				res = max(res,j-i)
			else:
				letter_set.remove(s[i])
				i += 1
		return res