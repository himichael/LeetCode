# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if(k==0 or head==None):
            return head
        p = head
        count = 0
        while(p != None):
            p = p.next
            count += 1
        k = k%count
        if(k == 0):
            return head
        i = 0
        p = ListNode(-1)
        p.next = head   
        while(i < count-k):
            p = p.next
            i += 1
        
        #假设链表是1->2->3->4->5 rotate是2，此时p为3，也就是新的tail
        #新的new_head就是4，也就是p.next
        #因为4后面还有元素，所以需要继续遍历到结束，然后将最后的元素->到原始的链表头(这里是head)
        new_tail = p
        new_head = p.next
        while(p.next != None):
            p = p.next
        p.next = head
        new_tail.next = None
        return new_head
        