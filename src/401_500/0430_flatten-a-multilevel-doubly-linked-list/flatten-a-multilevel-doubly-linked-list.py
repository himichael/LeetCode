"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution(object):
	def flatten(self, head):
		dummy = Node(-1,None,head,None)
		stack = []
		cur = head
		while cur:
			if cur.child:
				if cur.next:
					stack.append(cur.next)
				cur.next = cur.child
				cur.child = None
				cur.next.prev = cur
			else:
				if not cur.next and stack:
					cur.next = stack.pop()
					cur.next.prev = cur
			cur = cur.next
		return dummy.next