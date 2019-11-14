class Solution(object):
	
	# 队列实现
	def letterCombinations(self, digits):
		"""
		:type digits: str
		:rtype: List[str]
		"""	
		if not digits:
			return []
		d = [" ","*","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
		
		res = [""]
		for i in digits:
			#tmp = res.pop(0)
			size = len(res)
			letters = d[ord(i)-48]
			
			for _ in xrange(size):
				tmp = res.pop(0)
				for j in letters:
					res.append(tmp+j)
		return res
		
	# 递归实现
	def letterCombinations(self, digits):
		"""
		:type digits: str
		:rtype: List[str]
		"""
		if not digits:
			return []
		d = [" ","*","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]		
		res = []
		def dfs(s,tmp):
			if not s:
				res.append(tmp)
				return
			letter = d[ord(s[0])-48]
			for i in letter:
				dfs(s[1:],tmp+i)
		dfs(digits,"")
		return res