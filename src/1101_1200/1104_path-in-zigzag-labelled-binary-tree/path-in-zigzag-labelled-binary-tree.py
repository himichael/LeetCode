class Solution(object):
	def pathInZigZagTree(self, label):
		"""
		:type label: int
		:rtype: List[int]
		"""
		
		count = 0
		num = label
		while num > 0:
			num >>= 1
			count += 1
		#print count
		
		arr = [1] * count
		arr[count-1] = label
		count -= 1
		while count > 1:
			tmp = arr[count]
			end = 2**count -1
			count -= 1
			start = 2**count
			
			tmp /= 2
			value = end - abs(tmp-start)
			arr[count] = value
		#print arr
		return arr