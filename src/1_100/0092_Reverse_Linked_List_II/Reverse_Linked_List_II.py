# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	# 先找到反转字符串的前一个str_pre，然后根据 k<n，不断反转链表
	# 最后将str_pre->next = pre
	# tmp是反转链表的后面一个节点，str_tail是反转链表后的尾巴
	# 将 str_tail->next = tmp 整个链表就 串联起来了
    def reverseBetween(self, head, m, n):
        p = ListNode(-1)
        cur,k,p.next = p,0,head
        while cur and k<m-1:
            cur,k = cur.next,k+1
        str_pre,str_tail = cur,cur.next
        str_pre.next,pre,tmp,cur = None,None,None,str_tail
        while cur and k<n:
            tmp,cur.next,pre,cur,k = cur.next,pre,cur,cur.next,k+1
        str_pre.next,str_tail.next = pre,tmp
        return p.next