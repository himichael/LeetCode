class Solution {
	public List<List<Integer>> permute(int[] nums) {
		if(nums==null || nums.length==0) {
			new ArrayList<List<Integer>>();
		}

		Queue<Integer> queue = new LinkedList<>();
		for(int i=0;i<nums.length;i++) {
		queue.add(nums[i]);
		}
		iter(queue, new Stack<>());
		return list;
	}
	
	List<List<Integer>> list = new ArrayList<List<Integer>>();
	
	//这里使用了 队列+栈的方式来完成全排列，使用队列每次取队头的元素，然后调用下一个递归，递归结束后再把第一个元素放到队尾巴
	// (0) 1->2->3 准备调用第一个递归函数
	// (1) 2->3 调用第二个递归函数   2->3->1
	// (2) 3    调用第三个递归函数   3->2     
	
	//这里还使用了一个栈，每次从队列中取出一个元素就放到栈中，再继续调用下一层递归函数
	//直到队列中的元素==0，这时候栈就满了，然后将元素放到最终的 list集合中
	//等最后一层调用完了，栈执行了一次pop()，把刚刚放入的元素弹出来，然后又会被放进一个元素
	
	// statck  1->2     调用递归函数       1->
	// statck: 1->2->3  调用递归函数   	   1->2
	// 递归终止，记录1->2->3 并返回 
	void iter(Queue<Integer> queue, Stack<Integer> head) {
		if(queue.size() == 0) {
			//System.out.println(head);
			List<Integer> arr = new ArrayList<>(head);
			list.add(arr);
			return;
		}
		int size = queue.size();

		for(int i=0;i<size;i++) {
			Integer tmp = queue.poll();
			head.push(tmp);
			iter(queue,  head);
			queue.offer(tmp);
			head.pop();
		}
	}
}