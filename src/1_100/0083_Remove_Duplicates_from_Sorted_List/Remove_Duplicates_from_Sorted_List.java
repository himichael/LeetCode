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
        if(head==null) {
            return head;
        }
        ListNode i = head;
        ListNode j = head;
        while(j != null) {
            if(i.val != j.val) {
                i = i.next;
                i.val = j.val;
            }
            j = j.next;
        }
        i.next = null;
        return head;
    }
}