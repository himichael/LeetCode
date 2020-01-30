class Solution(object):
	def isSubsequence(self, s, t):
		"""
		:type s: str
		:type t: str
		:rtype: bool
		"""
		i,j = 0,0
		while i<len(s) and j<len(t):
			if s[i]==t[j]:
				i,j = i+1,j+1
			else:
				j += 1
		return True if i==len(s) else False
	
	# 另一种解法
	def isSubsequence(self, s, t):
		"""
		:type s: str
		:type t: str
		:rtype: bool
		"""
		if not s:
			return True
		if not t:
			return False
		i,j = 0,0
		while i<len(s):
			cur = s[i]
			while j<len(t):
				if cur==t[j]:
					i,j = i+1,j+1
					break
				j += 1
			if j==len(t) and i<len(s):
				return False
			if i==len(s):
				return True