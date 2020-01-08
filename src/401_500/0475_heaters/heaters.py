class Solution(object):
	def findRadius(self, houses, heaters):
		"""
		:type houses: List[int]
		:type heaters: List[int]
		:rtype: int
		"""
		houses.sort()
		heaters.sort()
		res = []
		for i in houses:
			begin,end = 0,len(heaters)-1
			while begin<end:
				mid = begin+(end-begin)/2
				if heaters[mid]<i:
					begin = mid+1
				else:
					end = mid
			if heaters[begin]==i:
				res.append(0)
			elif heaters[begin]<i:
				res.append(i-heaters[begin])
			elif begin>0:
				res.append( min(heaters[begin]-i,i-heaters[begin-1]) )
			else:	
				res.append(heaters[begin]-i)		
		return max(res)