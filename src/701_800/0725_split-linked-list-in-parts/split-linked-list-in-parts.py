# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	def splitListToParts(self, root, k):
		"""
		:type root: ListNode
		:type k: int
		:rtype: List[ListNode]
		"""
		if not root:
			return [None]*k
		res,p,q,n = [None]*k,root,root,0
		while p:
			p,n = p.next,n+1
		per_len,per = 1 if n/k==0 else n/k,1
		extra_count,index = 0 if n<=k else n%k,0	
		
		#print "per_len-->"+str(per_len)+"  extra_count-->"+str(extra_count)
		per_link_start = q
		while q:
			if per==per_len:
				tmp = q.next
				if extra_count:
					p,tmp.next = tmp.next,None
					tmp,extra_count = p,extra_count-1
				else:
					q.next = None
				res[index],q,index = per_link_start,tmp,index+1
				per_link_start = tmp
				per = 1
				continue
			q,per = q.next,per+1
			#print "cur PER -->"+str(per)
		return res