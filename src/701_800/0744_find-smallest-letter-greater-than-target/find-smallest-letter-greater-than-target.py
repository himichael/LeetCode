class Solution(object):
	def nextGreatestLetter(self, letters, target):
		"""
		:type letters: List[str]
		:type target: str
		:rtype: str
		"""	
		begin,end = 0,len(letters)-1
		while begin<=end:
			mid = begin+(end-begin)/2
			if letters[mid]<=target:
				begin = mid+1
			else:
				end = mid-1
		return letters[begin%len(letters)]