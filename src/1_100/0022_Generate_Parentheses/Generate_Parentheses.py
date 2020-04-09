class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if(n == 0):
            return []
        res = []
        def recursion(left,right,content):
            if(left==n and right==n):
                res.append(content)
                return
            if(left>n or right>n or left<right):
                return
            recursion(left+1, right, content+"(")
            recursion(left, right+1, content+")")
        recursion(0, 0, "")
        return res
		
		
		
	# 简化的 DFS实现
	def generateParenthesis(self, n):
		if n<=0:
			return []
		res = []
		def dfs(left,right,tmp):
			if left==n and right==n:
				res.append(tmp)
				return
			if left<n:
				dfs(left+1,right,tmp+"(")
			if right<left and right<n:
				dfs(left,right+1,tmp+")")
		dfs(0,0,"")
		return res	
	
	
	
	# BFS实现
	def generateParenthesis(self, n):
		if n<=0:
			return []
		res = []
		queue = [(0,0,"")]
		while queue:
			left,right,tmp = queue.pop(0)
			if left==n and right==n:
				res.append(tmp)
				continue
			if left<n:
				queue.append((left+1,right,tmp+"("))
			if right<left and right<n:
				queue.append((left,right+1,tmp+")"))
		return res