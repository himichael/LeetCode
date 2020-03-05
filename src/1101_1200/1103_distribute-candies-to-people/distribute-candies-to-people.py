class Solution(object):
	def distributeCandies(self, candies, num_people):
		"""
		:type candies: int
		:type num_people: int
		:rtype: List[int]
		"""
		if candies<=0 or num_people<=0:
			return []
		res = [0 for _ in xrange(num_people)]
		i = 0
		j = 1
		while candies>0:
			if j>=candies:
				j = candies
			res[i%num_people] += j
			candies -= j
			i += 1
			j += 1
		return res
		
		
		
	# 更简洁的实现	
	def distributeCandies(self, candies, num_people):
		"""
		:type candies: int
		:type num_people: int
		:rtype: List[int]
		"""
		if candies<=0 or num_people<=0:
			return []
		res = [0 for _ in xrange(num_people)]
		i = 0
		while candies>0:
			res[i%num_people] += min(i+1,candies)
			candies -= min(i+1,candies)
			i += 1
		return res