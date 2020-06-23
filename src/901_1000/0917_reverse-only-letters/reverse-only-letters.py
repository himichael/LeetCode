class Solution(object):
	def reverseOnlyLetters(self, S):
		"""
		:type S: str
		:rtype: str
		"""
		if not S:
			return S
		n = len(S)
		i = 0
		j = n-1
		arr = list(S)
		while i<j:
			if not arr[i].isalpha():
				i += 1
			elif not arr[j].isalpha():
				j -= 1
			else:
				arr[i],arr[j] = arr[j],arr[i]
				i += 1
				j -= 1
		return "".join(arr)