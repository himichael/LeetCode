/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
	//用栈实现，将k个元素放入栈中，再依次弹出加入链表中
    public ListNode reverseKGroup(ListNode head, int k) {
		if(head==null || head.next==null) {
			return head;
		}
		ListNode dummy = new ListNode(-1);
		ListNode p = head;
		head = dummy;
		LinkedList<ListNode> stack = new LinkedList<ListNode>();
		while(p!=null && p.next!=null) {
			for(int i=0;i<k;i++) {
				stack.add(p);
				p = p.next;
				if(p==null) {
					break;
				}
			}
			int len = stack.size();
			//这里需要处理边界问题，如果输入的是: [1,2,3,4] 2    最后遍历完3 4，stack中的数据就是[3,4]，size 等于 k，所以要反序处理
			//如果是输入 [1,2,3,4,5] 2 ，最后遍历到5，此时栈中的元素只有一个[5]，stack.size < k，所以要正序处理
			for(int i=0;i<len;i++) {
				if(len%k == 0) {
					dummy.next = stack.removeLast();
				}
				else {
					dummy.next = stack.removeFirst();
				}
				dummy = dummy.next;
			}
			dummy.next = null;
		}
		//收尾操作
		while(p != null) {
			dummy.next = p;
			p = p.next;
			dummy = dummy.next;
		}
		//dummy的next==null，防止出现循环链表
		dummy.next = null;
		return head.next;
    }
}