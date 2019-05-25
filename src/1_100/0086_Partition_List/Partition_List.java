/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode partition(ListNode head, int x) {
    	if(head==null ||head.next==null) {
    		return head;
    	}
    	ListNode cur = head;
    	ListNode cur_min = new ListNode(-1);
    	ListNode pre_min = cur_min;
    	ListNode cur_max = new ListNode(-1);
    	ListNode pre_max = cur_max;
    	while(cur != null) {
    		if(cur.val < x) {
    			cur_min.next = cur;
    			cur_min = cur_min.next;
    		} else {
    			cur_max.next = cur;
    			cur_max = cur_max.next;
    		}
    		cur = cur.next;
    	}
    	cur_min.next = pre_max.next;
    	cur_max.next = null;
        return pre_min.next;
    }
}