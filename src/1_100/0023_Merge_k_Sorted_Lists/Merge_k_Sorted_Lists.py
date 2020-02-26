class Solution(object):
	def mergeKLists(self, lists):
		if not lists or len(lists)==1:
			return lists[0] if lists else None
		import heapq
		queue = []
		dummy = ListNode(-1)
		p = dummy
		for i in xrange(len(lists)):
			cur = lists[i]
			while cur:
				heapq.heappush(queue,cur.val)
				cur = cur.next
		while queue:
			val = heapq.heappop(queue)
			p.next = ListNode(val)
			p = p.next
		p.next = None
		return dummy.next