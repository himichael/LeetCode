class Solution(object):
	def canCross(self, stones):
		n = len(stones)
		d = {}
		cache = {}
		for i in range(n):
			d[stones[i]] = i
		def dfs(index, step):
			if (index,step) in cache:
				return cache[index,step]
			if index == n - 1:
				return True
			for i in (-1, 0, 1):
				if step + i == 0:
					continue
				tmp = stones[index] + step + i
				if tmp in d:
					if dfs(d[tmp], step + i):
						cache[index,step] = True
						return True
			cache[index,step] = False
			return False
		if stones[1] - stones[0] != 1:
			return False
		return dfs(1, 1)