class Solution(object):
	def countSmaller(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[int]
		"""
		if not nums or len(nums)<2:
			return [0] if nums else []
		n = len(nums)
		indexes = [i for i in xrange(n)]
		tmp = [0 for _ in xrange(n)]
		count = [0 for _ in xrange(n)]
		def count_paris(left,right):
			if left==right:
				return
			mid = left+(right-left)//2
			count_paris(left,mid)
			count_paris(mid+1,right)
			if nums[indexes[mid]]<=nums[indexes[mid+1]]:
				return
			merge_count(left,mid,right)
		
		def merge_count(left,mid,right):
			for i in xrange(left,right+1):
				tmp[i] = indexes[i]
			i = left
			j = mid+1
			for k in xrange(left,right+1):
				if i>mid:
					indexes[k] = tmp[j]
					j += 1
				elif j>right:
					indexes[k] = tmp[i]
					i += 1
					count[indexes[k]] += (right-mid)
				elif nums[tmp[i]]<=nums[tmp[j]]:
					indexes[k] = tmp[i]
					i += 1
					count[indexes[k]] += (j-mid-1)
				else:
					indexes[k] = tmp[j]
					#count[index[k]] += (mid-i+1)
					j += 1
		count_paris(0,n-1)
		return count