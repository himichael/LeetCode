class Solution(object):
	def isMatch(self, text, pattern):
		"""
		:type s: str
		:type p: str
		:rtype: bool
		"""
		if(not pattern):
			return not text
		first_match = bool(text) and (pattern[0]==text[0] or pattern[0]=='.')
		if( len(pattern)>=2 and pattern[1]=='*'):
			return self.isMatch(text,pattern[2:]) or (first_match and self.isMatch(text[1:],pattern))
		else:
			return first_match and self.isMatch(text[1:],pattern[1:])
			