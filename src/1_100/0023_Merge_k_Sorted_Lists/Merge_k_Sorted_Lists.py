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
		
		
		
	# 分治
	def mergeKLists(self, lists):
		if not lists or len(lists)==1:
			return lists[0] if lists else None
		def helper(begin,end):
			if begin==end:
				return lists[begin]
			mid = begin+(end-begin)/2
			left = helper(begin,mid)
			right = helper(mid+1,end)
			return merge(left,right)
		def merge(a,b):
			if not (a and b):
				return a if a else b
			if a.val<=b.val:
				a.next = merge(a.next,b)
				return a
			else:
				b.next = merge(a,b.next)
				return b
		return helper(0,len(lists)-1)