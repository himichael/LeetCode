/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode a, ListNode b) {
        ListNode head = new ListNode(-1);
        ListNode p = head;
        boolean isPlus = false;
        while(a!=null && b!=null) {
            int tmp = a.val+b.val;
            if(isPlus) {
                if(tmp+1 > 9) {
                    tmp = (tmp+1)%10;
                    isPlus = true;
                }else {
                    tmp = tmp+1;
                    isPlus = false;
                }
            }
            else {
                if(tmp > 9) {
                    tmp = tmp%10;
                    isPlus = true;
                }else {
                    isPlus = false;
                }
            }
            ListNode node = new ListNode(tmp);
            p.next = node;
            p = node;
            a = a.next;
            b = b.next;
        }

        if(a!=null) {
            while(a!=null) {
                int tmp = a.val;
                if(isPlus) {
                    if(tmp+1 > 9) {
                        tmp = (tmp+1)%10;
                        isPlus = true;
                    }else {
                        tmp = tmp+1;
                        isPlus = false;
                    }
                }
                else {
                    if(tmp > 9) {
                        tmp = tmp%10;
                        isPlus = true;
                    }else {
                        isPlus = false;
                    }
                }
                ListNode node = new ListNode(tmp);
                p.next = node;
                p = node;
                a = a.next;
            }
        }

        if(b!=null) {
            while(b!=null) {
                int tmp = b.val;
                if(isPlus) {
                    if(tmp+1 > 9) {
                        tmp = (tmp+1)%10;
                        isPlus = true;
                    }else {
                        tmp = tmp+1;
                        isPlus = false;
                    }
                }
                else {
                    if(tmp > 9) {
                        tmp = tmp%10;
                        isPlus = true;
                    }else {
                        isPlus = false;
                    }
                }
                ListNode node = new ListNode(tmp);
                p.next = node;
                p = node;
                b = b.next;
            }
        }
        if(isPlus) {
            ListNode node = new ListNode(1);
            p.next = node;
        }

        return head.next;
    }

}