class Solution(object):
	def maxSlidingWindow(self, nums, k):
		if not nums or k <= 0:
			return []
		q = collections.deque()
		n = len(nums)
		for i in xrange(k):
			while q and nums[q[-1]] <= nums[i]:
				q.pop()
			q.append(i)
		ans = [nums[q[0]]]
		for i in xrange(k, n):
			while q and nums[q[-1]] <= nums[i]:
				q.pop()
			q.append(i)
			while q[0] <= i - k:
				q.popleft()
			ans.append(nums[q[0]])
		return ans