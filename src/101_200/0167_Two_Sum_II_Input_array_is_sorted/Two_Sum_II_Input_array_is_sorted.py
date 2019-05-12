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