class Solution(object):
	def reverseKGroup(self, head, k):
		if not head or k<=0:
			return head
		p = ListNode(-1)
		p.next = head
		cur = p
		n = k
		def reverse(head):
			pre,cur = None,head
			while cur:
				cur.next,pre,cur = pre,cur,cur.next
			return pre
		while cur.next:
			tmp = cur
			while tmp and tmp.next and n>0:
				tmp = tmp.next
				n -= 1
			if n==0:
				next_node = tmp.next
				tail = cur.next
				tmp.next = None
				cur.next = reverse(tail)
				tail.next = next_node
				cur = tail
				n = k
			else:
				break
		return p.next