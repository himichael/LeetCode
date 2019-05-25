/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode reverseBetween(ListNode head, int m, int n) {
    	if(head==null || m<=0 || n<=0 || m>=n) {
    		return head;
    	}
    	ListNode dummy = new ListNode(-1);
    	ListNode p = dummy;
    	p.next = head;
    	int i = 0;
    	while(p!=null && i<m-1) {
    		p = p.next;
    		i++;
    	}
    	if(p == null) {
    		return head;
    	}
    	LinkedList<ListNode> stack = new LinkedList<ListNode>();
    	ListNode cur = p.next;
    	ListNode next = null;
    	while(cur!=null && i<n) {
    		stack.push(cur);
    		next = cur.next;
    		cur = cur.next;
    		i++;
    	}
    	p.next = null;
    	while(!stack.isEmpty()) {
    		p.next = stack.pop();
    		p = p.next;
    		p.next = null;
    	}
    	p.next = null;
    	p.next = next;
    	return dummy.next;
    }
}