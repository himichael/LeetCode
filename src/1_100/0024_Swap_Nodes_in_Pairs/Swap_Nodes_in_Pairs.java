/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
	
	//另一种实现方式，基于栈，遍历的时候往栈中push两个元素，再弹出两个元素，就可以达到翻转的效果
	public ListNode swapPairs_2(ListNode head) {
		if(head==null || head.next==null) {
			return head;
		}
		ListNode dummy = new ListNode(-1);
		ListNode p = head;
		head = dummy;
		Stack<ListNode> stack = new Stack<ListNode>();
		while(p!=null && p.next!=null) {
			stack.add(p);
			stack.add(p.next);
			p = p.next.next;
			dummy.next = stack.pop();
			dummy = dummy.next;
			dummy.next = stack.pop();
			dummy = dummy.next;
		}
		if(p != null) {
			dummy.next = p;
		} else {
			dummy.next = null;
		}
		//dump(head,"head");
		return head.next;
	}
	
    public ListNode swapPairs(ListNode head) {
        if(head==null || head.next==null) {
            return head;
        }
        ListNode saveToRes = new ListNode(-1);
        saveToRes.next = head.next;
        ListNode p = new ListNode(-1);
        p.next = head;
        ListNode a = null;
        ListNode b = null;
        ListNode tmp = null;
        while(p.next!=null && p.next.next!=null) {
            a = p.next;
            b = p.next.next;
            tmp = b.next;
            b.next = a;
            a.next = tmp;
            p.next = b;
            p = a;
        }
        //System.out.println("??????");
        return saveToRes.next;
    }
}
            