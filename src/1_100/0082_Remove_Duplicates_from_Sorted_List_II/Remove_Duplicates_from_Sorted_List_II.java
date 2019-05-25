/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
    	if(head == null) {
    		return head;
    	}
    	ListNode dummy = new ListNode(-1);
    	ListNode low = head;
    	ListNode fast = head.next;
    	dummy.next = head;
    	ListNode p = dummy;
    	while(fast!=null && fast.next!=null) {
    		if(low.val != fast.val) {
    			p.next = low;
    			p = p.next;
    			low = fast;
    			fast = fast.next;
    		} else {
    			while(fast.next!=null && fast.next.val==low.val) {
    				fast = fast.next;
    			}
    			low = fast.next;
    			fast = fast.next!=null? fast.next.next : null;
    		}
    	}
    	if(fast != null) {
    		if(low.val == fast.val) {
    			p.next = null;
    		}else {
    			p.next = low;
    			p.next.next = fast;
    		}
    	} else {
    		p.next = low!=null? low : null;
    	}
    	return dummy.next;
    }
}