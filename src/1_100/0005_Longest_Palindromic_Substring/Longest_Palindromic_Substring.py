class Solution(object):
	def longestPalindrome(self, s):
		"""
		:type s: str
		:rtype: str
		"""	
		if not s or len(s)==0:
			return ""
		def expand_center(left,right):
			L,R = left,right
			while L>=0 and R<len(s) and s[L]==s[R]:
				L -= 1
				R += 1
			return R-L-1
		start,end = 0,0
		for i in xrange(len(s)):
			odd = expand_center(i,i)
			even = expand_center(i,i+1)
			max_len = max(odd,even)
			if max_len>(end-start):
				start = i-(max_len-1)/2
				end = i+1+(max_len)/2
		return s[start:end]