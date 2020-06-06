class Solution(object):
	def longestConsecutive(self, nums):
		if not nums:
			return 0
		d = dict()
		res = 0
		for i in nums:
			if i not in d:
				left  = d[i-1] if i-1 in d else 0
				right = d[i+1] if i+1 in d else 0
				n = left+right+1
				d[i] = n
				d[i-left] = n
				d[i+right] = n
				res = max(res,n)
		return res
		
		
		
	#另一种解法	
	def longestConsecutive(self, nums):
		if not nums:
			return 0
		nums_set = set(nums)
		longest_seq = 0
		for i in nums_set:
			if i-1 not in nums_set:
				cur_num = i
				cur_seq = 1
				while cur_num+1 in nums_set:
					cur_num += 1
					cur_seq += 1
				longest_seq = max(longest_seq,cur_seq)
		return longest_seq
		
		
		