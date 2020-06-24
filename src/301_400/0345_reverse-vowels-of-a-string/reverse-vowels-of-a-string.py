class Solution(object):
	def reverseVowels(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		if not s:
			return s
		n = len(s)
		i = 0
		j = n-1
		d = set(['a','e','i','o','u','A','E','I','O','U'])
		s = list(s)
		while i<j:
			while i<j and s[i] not in d:
				i += 1
			while i<j and s[j] not in d:
				j -= 1
			s[i],s[j] = s[j],s[i]
			i += 1
			j -= 1
		return "".join(s)