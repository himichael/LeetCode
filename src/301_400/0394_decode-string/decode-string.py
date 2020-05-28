class Solution:
	def decodeString(self, s):
		if not s:
			return ""
		res = ""
		multi = 0
		stack = []
		for c in s:
			if "0"<=c<="9":
				multi = multi*10 + int(c)
			elif c=="[":
				stack.append( (res,multi) )
				res = ""
				multi = 0
			elif c=="]":
				pre_str,in_multi = stack.pop()
				res = pre_str + in_multi*res
			else:
				res += c
		return res