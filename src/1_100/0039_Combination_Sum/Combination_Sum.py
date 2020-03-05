class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates)
        res = []
        def recursive(candidates, index, cur_list, target):
            if(target == 0):
                res.append( cur_list[:] )
                return
            for i in range(index,len(candidates)):
                if(candidates[i] > target):
                    break;
                cur_list.append(candidates[i])
                recursive(candidates, i, cur_list, target-candidates[i])
                cur_list.pop()
        recursive(candidates, 0, [], target)
        return res
		
		
			
	# 优化递归代码
	def combinationSum(self, candidates, target):
		if not candidates:
			return []
		n = len(candidates)
		res = []
		candidates = sorted(candidates)
		def dfs(index,arr,tmp):
			if tmp==target:
				res.append(arr)
				return
			for i in xrange(index,n):
				val = candidates[i]
				if tmp+val>target or val>target:
					break
				dfs(i,arr+[val],tmp+val)
		dfs(0,[],0)
		return res
		
		
		
	# 另一种DFS实现
	def combinationSum(self, candidates, target):
		if not candidates:
			return []
		n = len(candidates)
		res = []
		candidates = sorted(candidates)
		def dfs(index,arr,tmp):
			if tmp==target:
				res.append(arr)
				return
			if index==n:
				return
			val = candidates[index]
			if val>target or tmp+val>target:
				return 
			dfs(index,arr+[val],tmp+val)
			dfs(index+1,arr,tmp)
		dfs(0,[],0)
		return res
		
		