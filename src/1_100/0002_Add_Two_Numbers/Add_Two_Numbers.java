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
		
		//遍历两个链表，同时相加a，b两个链表的val
		//如果val>9，说明要进位，记录进位标志，下一次迭代的时候计算
		//a.val+b.val+1 这里的1是进位过来的，如果这个数还是>9继续进位，否则直接记录下来即可
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

		//如果两个链表遍历完了，但是a或者b还没结束，则将a或b后面的值加入到合并的链表中
		//注意这里也需要考虑进位问题
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
		
		//如果a，b一样长，都遍历完了，但是有进位情况，就再增加一个Node，node的值记为1即可
        if(isPlus) {
            ListNode node = new ListNode(1);
            p.next = node;
        }

        return head.next;
    }

}