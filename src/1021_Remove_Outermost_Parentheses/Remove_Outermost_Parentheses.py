class Solution(object):
	def removeOuterParentheses(self, S):
		n = 0
		res = ""
		for i in S:
			if i=="(":
				if n>0:
					res += i
				n += 1
			else:
				if n>1:
					res += i
				n -= 1
		return res