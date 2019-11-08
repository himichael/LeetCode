class Solution {
    public ListNode rotateRight(ListNode head, int k) {
		if(head==null || k<=0) {
			return head;
		}
		ListNode p = new ListNode(-1);
		p.next = head;
		ListNode cur = p;
		ListNode low = p;
		ListNode fast = p;
		int n = 0;
		while(cur.next!=null) {
			cur = cur.next;
			++n;
		}
		if(n==0 || k%n==0) {
			return head;
		}
		n = k%n;
		while(fast.next!=null && n>0) {
			fast = fast.next;
			--n;
		}
		while(fast.next!=null) {
			low = low.next;
			fast = fast.next;
		}
		fast.next = p.next;
		p.next = low.next;
		low.next = null;
		return p.next;
	}
}