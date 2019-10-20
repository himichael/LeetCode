"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution(object):
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