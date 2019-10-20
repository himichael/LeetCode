"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution(object):
	# hash表实现方式
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        p,q,d = head,head,dict()
        while q:
            d[q],q = Node(q.val,None,None),q.next
        while p:
            d[p].next = d[p.next] if p.next else None
            d[p].random = d[p.random] if p.random else None
            p = p.next
        return d[head] if head else None
		
		
		
	# 增加冗余节点 O(1)空间复杂度实现方式
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head
        q = Node(-1,None,None)
        p,p2,p3,cur = head,head,head,q
        while p:
            x = Node(p.val,None,None)
            x.next = p.next
            p.next,p = x,x.next
        while p2:
            p2.next.random = p2.random.next if p2.random else None
            p2 = p2.next.next
        while p3:
            cur.next,cur = p3.next,p3.next
            p3.next,p3 = cur.next,cur.next
        return q.next