class Solution(object):
	def combinationSum3(self, k, n):
		"""
		:type k: int
		:type n: int
		:rtype: List[List[int]]
		"""
		arr = [1,2,3,4,5,6,7,8,9]
		res = []
		def back_trace(i,tmp,stack):
			if(tmp==n and len(stack)==k):
				res.append(list(stack))
				return
			for j in range(i,len(arr)):
				if(arr[j]+tmp<=n and len(stack)<=k):
					stack.append(arr[j])
					back_trace(j+1,tmp+arr[j],stack)
					stack.pop()
		back_trace(0,0,[])
		return res