/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
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
            