# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = ListNode(-1)
        cur = node
        while(head != None):
            tmp = head
            head = head.next
            tmp.next = None
            cur = node
            found = False
            if(cur.next==None):
                cur.next = tmp
                continue
            while(cur.next!=None):
                if(cur.next.val >= tmp.val):
                    tmp.next = cur.next
                    cur.next = tmp
                    found = True
                    break
                cur = cur.next
            if(not found):
                cur.next = tmp
        return node.next
		
		
	# 精简代码实现
	def insertionSortList(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		p,cur = ListNode(-1),head
		while cur:
			tmp,cur = cur,cur.next
			tmp.next,q,found = None,p,False
			while q and q.next:
				if q.next.val > tmp.val:
					tmp.next = q.next
					q.next,found = tmp,True
					break
				q = q.next
			if not found:
				q.next = tmp
		return p.next	
		
		