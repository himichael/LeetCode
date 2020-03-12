class Solution(object):
	def gcdOfStrings(self, str1, str2):
		"""
		:type str1: str
		:type str2: str
		:rtype: str
		"""
		def gdc(a,b):
			if not b:
				return a
			return gdc(b,a%b)
		if (str1+str2)!=(str2+str1):
			return ""
		gdc_size = gdc(len(str1),len(str2))
		return str1[:gdc_size]