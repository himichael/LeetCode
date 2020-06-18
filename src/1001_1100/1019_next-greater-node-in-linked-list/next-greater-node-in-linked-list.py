class Solution(object):
	def nextLargerNodes(self, head):
		"""
		:type head: ListNode
		:rtype: List[int]
		"""	
		if not head:
			return []
		stack = []
		arr = []
		while head:
			arr.append(head.val)
			head = head.next
		n = len(arr)
		res = [0 for _ in xrange(n)]
		for i in xrange(n):
			while stack and arr[i]>arr[stack[-1]]:
				res[stack[-1]] = arr[i]
				stack.pop()
			stack.append(i)
		return res