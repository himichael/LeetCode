﻿/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode head = new ListNode(-1);
        ListNode p = head;
        while(l1!=null && l2!=null) {
            if(l1.val < l2.val) {
                p.next = l1;
                l1 = l1.next;
            } else {
                p.next = l2;
                l2 = l2.next;
            }
            p = p.next;
        }
        while(l1!=null || l2!=null) {
            p.next = l1!=null? l1 : l2;
            l1 = l1==null? null : l1.next;
            l2 = l2==null? null : l2.next;
            p = p.next;
        }
        return head.next;
    }
}