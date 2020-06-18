class Solution(object):
	def removeZeroSumSublists(self, head):
		if not head:
			return None
		dummy = ListNode(0)
		dummy.next = head
		p = dummy
		d = dict()
		sum = 0
		while p:
			sum += p.val
			d[sum] = p
			p = p.next
		sum = 0
		p = dummy
		while p:
			sum += p.val
			p.next = d[sum].next
			p = p.next
		return dummy.next