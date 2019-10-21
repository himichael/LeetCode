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
		"""
		:type head: Node
		:rtype: Node
		"""
		stack,p = [],head
		while p:
			if p.child:
				if p.next:
					stack.append(p.next)
				p.next,p.child.prev = p.child,p
				p.child = None
			else:
				if not p.next and stack:
					p.next = stack.pop()
					p.next.prev = p
			p = p.next
		return head