class Solution(object):
	def twoSum(self, numbers, target):
		m = dict()
		for i in range(len(numbers)):
			m[numbers[i]] = i
			
		for i in range(len(numbers)):
			n = target - numbers[i]
			if(m.has_key(n)):
				tmp = m[n]
				if(i<tmp):
					return [i+1,tmp+1]
				else:
					return [tmp+1,i+1]
		return [-1,-1]
		

	def twoSum_2(self, numbers, target):
		"""
		:type numbers: List[int]
		:type target: int
		:rtype: List[int]
		"""
		if not numbers:
			return [-1,-1]
		begin,end = 0,len(numbers)-1
		while begin<end:
			x = numbers[begin]+numbers[end]
			if x > target:
				end -= 1
			elif x < target:
				begin += 1
			else:
				return [begin+1,end+1]
		return [-1,-1]